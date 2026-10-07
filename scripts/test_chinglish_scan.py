"""Regression checks for extraction and advisory behavior; no model evaluation."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("scanner", Path(__file__).with_name("chinglish_scan.py"))
scanner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scanner)


class ScannerTests(unittest.TestCase):
    def scan(self, text, plain=False):
        return scanner.scan(text.splitlines(), plain)

    def test_english_typography_is_valid(self):
        warns, _, _ = self.scan('“It’s ready…” she said—then paused. It was a 2–3 day trip.')
        self.assertFalse(warns)

    def test_chinese_punctuation_is_candidate(self):
        warns, _, _ = self.scan('The result，as reported，was stable。')
        self.assertEqual([w[1] for w in warns], ['中文标点'])

    def test_source_quotes_default_and_plain(self):
        sample = '> We make great efforts to help。\n\nClear text.'
        self.assertFalse(self.scan(sample)[0])
        self.assertEqual({w[0] for w in self.scan(sample, True)[0]}, {1})

    def test_fences_ignore_bodies_and_keep_real_line_numbers(self):
        sample = '````python\nmake great efforts to\n```\n```\n````\n~~~text\nThe fact that，\n~~~\nThe fact that it rained matters.'
        warns, _, words = self.scan(sample)
        self.assertEqual({w[0] for w in warns}, {9})
        self.assertEqual(words, 6)

    def test_indented_code_and_list_continuation(self):
        sample = '    The fact that code，\n\tmake great efforts to\n\n- Clear start\n    We make great efforts to help.'
        self.assertEqual({w[0] for w in self.scan(sample)[0]}, {5})

    def test_inline_code_matching_runs_and_unclosed_literal(self):
        sample = 'Keep `the fact that` and ``make ` great efforts to``.\nThe `unclosed marker cannot hide the fact that this matters.'
        self.assertEqual({w[0] for w in self.scan(sample)[0]}, {2})
        multi = 'Start `the fact that\nmake great efforts to` end.\nThe fact that this works matters.'
        self.assertEqual({w[0] for w in self.scan(multi)[0]}, {3})

    def test_links_scan_labels_not_destinations(self):
        sample = '[Clear label](https://example.org/a(the_fact_that) "make great efforts to")\n[the fact that](https://example.org)\n![Image](https://example.org/actively)\n[Readable][ref]\n[ref]: https://example.org/actively "the fact that"\n<https://example.org/actively> https://example.org/actively\n<mailto:actively@example.org>'
        warns, counts, words = self.scan(sample)
        self.assertEqual({w[0] for w in warns}, {2})
        self.assertEqual(counts, {})
        self.assertEqual(words, 7)

    def test_frontmatter_and_html_comments(self):
        sample = '---\ntitle: the fact that\n---\n<!-- make great efforts to\nmore code -->\nThe fact that this matters is clear.'
        self.assertEqual({w[0] for w in self.scan(sample)[0]}, {6})

    def test_literal_html_comment_in_code_cannot_hide_prose(self):
        sample = '```html\n<!--\n```\nThe fact that it matters is clear.\nAn inline `<!--` example.\nWe make great efforts to help.'
        self.assertEqual({w[0] for w in self.scan(sample)[0]}, {4, 6})

    def test_table_cells_and_source_column(self):
        sample = '| 中文 | English |\n| --- | --- |\n| 原文 the fact that | We make great efforts to help。 |'
        warns, _, _ = self.scan(sample)
        self.assertEqual({w[0] for w in warns}, {3})
        self.assertNotIn('结构候选', [w[1] for w in warns])
        self.assertIn('动词短语', [w[1] for w in warns])
        self.assertIn('中文标点', [w[1] for w in warns])

    def test_table_without_outer_pipes_no_cross_cell_phrases(self):
        sample = 'Left | Right\n--- | ---\nthe fact | that\nName \\| label | the fact that it matters'
        warns, _, _ = self.scan(sample)
        self.assertEqual({w[0] for w in warns}, {4})

    def test_valid_based_on_and_contrastive_while(self):
        sample = 'Based on the data, the report recommends caution.\nWhile the first group improved, the second remained stable.'
        self.assertFalse(self.scan(sample)[0])

    def test_density_is_advisory_and_counts_ignore_code(self):
        warns, counts, _ = self.scan('Information transmission and communication remain stable.\nActively and effectively. `actively`')
        self.assertEqual([w[1] for w in warns], ['名词密度'])
        self.assertEqual(counts, {'actively': 1, 'effectively': 1})

    def test_zero_warnings_do_not_check_semantics(self):
        # A source may say "可能" and "只有...才". This fluent sentence loses both.
        sample = '> 只有校准后，系统才可能恢复。\nThe system always recovers.'
        self.assertFalse(self.scan(sample)[0])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'sample.md'
            path.write_text(sample, encoding='utf-8')
            result = subprocess.run([sys.executable, str(Path(scanner.__file__)), str(path)], text=True, capture_output=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('零警告不代表语义核查通过', result.stdout)

    def test_cli_warning_does_not_edit_and_read_error_is_nonzero(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'sample.md'
            source = 'The fact that we make great efforts to help matters。\n'
            path.write_text(source, encoding='utf-8')
            result = subprocess.run([sys.executable, str(Path(scanner.__file__)), str(path)], text=True, capture_output=True)
            self.assertEqual(result.returncode, 0)
            self.assertIn('L1:', result.stdout)
            self.assertEqual(path.read_text(encoding='utf-8'), source)
            missing = subprocess.run([sys.executable, str(Path(scanner.__file__)), str(path) + '.missing'], text=True, capture_output=True)
            self.assertEqual(missing.returncode, 2)


if __name__ == '__main__':
    unittest.main()
