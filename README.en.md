<div align="center">

# zh-en-translation-polish

### Translate Chinese into faithful, natural English, with paragraph-paired bilingual output

[![License: MIT](https://img.shields.io/badge/License-MIT-f5c542.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/version-1.1.1-2ea44f.svg)](./SKILL.md)
[![Agent Skills](https://img.shields.io/badge/agent-skills-black.svg)](https://github.com/vercel-labs/skills)

**English | [中文](./README.md)**

</div>

## What this skill does

This skill translates Chinese into English and polishes existing English translations against their Chinese source. It draws on Joan Pinkham’s *The Translator’s Guide to Chinglish* and Lu Guoqiang’s *汉译英常用表达式经典惯例*: establish meaning and semantic roles, choose natural English structures, then check the source and translation in both directions.

Fidelity applies to every register. Preserve facts, numbers, qualifications, logical relations, tone, and imagery. Keep attempts distinct from results, possibility from certainty, and sequence from causation. Simplify only when the meaning remains fully represented; fluency and brevity cannot substitute for accuracy.

## Uses and boundaries

| Use | Focus |
|---|---|
| Policy and official documents | Established terminology, policy scope, emphasis, goals, and commitments |
| Academic and technical writing | Terminology, evidence limits, modality, numbers, units, and appropriate syntax |
| Business correspondence and corporate websites | Politeness and the original strength of claims and promises; copywriting changes require user authorization |
| News, interviews, and industry reports | Concrete examples, speaker attribution, headings, and captions |
| Speeches, essays, and personal writing | Meaningful repetition, rhythm, metaphor, and individual voice |
| Existing English translations | Source-grounded checks for omissions, additions, and expression; accurate, natural wording can stay |

English-to-Chinese translation, polishing prose originally written in English, and individual word lookups are outside the full workflow. Without the Chinese source, the skill can assess English expression but cannot establish translation fidelity. Summaries, abridgments, and promotional adaptations follow the scope explicitly requested by the user.

## Installation

Install with the [skills CLI](https://github.com/vercel-labs/skills), selecting your target agent when prompted:

```bash
npx skills add -g HoraceLuBFA/zh-en-translation-polish
```

Alternatively, give the repository link to an agent that supports skill installation:

> Install this skill: https://github.com/HoraceLuBFA/zh-en-translation-polish

For a manual installation, clone into the shared skills directory. Inspect any existing directory before proceeding:

```bash
git clone https://github.com/HoraceLuBFA/zh-en-translation-polish.git ~/.agents/skills/zh-en-translation-polish
```

Check that `SKILL.md` exists and confirm availability in your host’s skill list. Discovery after a manual clone depends on host configuration; a file on disk does not prove that the skill is loaded. No other translation skill is required. The mechanical scanner needs Python 3 and uses only its standard library.

## Usage

Once installed and enabled, ask in natural language or name `zh-en-translation-polish` in a host that supports explicit invocation. Supply the Chinese text; for revision, include both the Chinese source and the English draft whenever possible.

- “Translate this Chinese passage into natural English, with bilingual output: …”
- “Translate this Chinese abstract into English only, preserving every qualification.”
- “Polish this English draft against its Chinese source; retain numbers, terms, and quotations.”
- “Translate this interview in full, preserving speakers, captions, and paragraph order, and save it to the specified file.”

Short passages are delivered in chat without a mandatory file or diagnostic report. Explicit English-only, bilingual, and destination-file requests take precedence. Existing target files are updated as requested.

For PDFs and other documents, the host’s available reading tools obtain the source. Text, captions, formulas, quotations, and references are preserved within the requested scope. Extraction gaps are reported rather than filled by inference.

## Workflow

| Stage | Work |
|---|---|
| 0 · Read and identify register | Establish scope, subjects, relations, parallel items, headings, and sentence focus |
| 1 · Draft | Organize English around meaning and roles without inventing facts to fit a structure |
| 2 · Diagnose expression | Review redundancy, nominalization, attachment, parallelism, order, connectives, and reference as needed |
| 3 · Check in both directions | Check coverage from the source and grounding from the translation; review modality, scope, numbers, and attribution |
| 4 · Scan | Run the advisory scanner on saved translations and assess its candidates |
| 5 · Deliver | Follow the requested format; derive an English-only file from the checked bilingual file when needed |

Long texts are translated and checked by section, speaker, or a few consecutive paragraphs, followed by a check of order, completeness, terminology, and reference after assembly. Length, paragraph counts, zero warnings, and model self-reports do not establish semantic quality. There is no compression target.

## File format and example

Full-document and project translations default to `<name> 翻译(汉英对照).md`, with each Chinese paragraph in a blockquote followed by its English translation. An optional `<name> 翻译(全英文).md` is derived mechanically from the checked bilingual file so the English is not rewritten separately. Shared images, tables, formulas, code, and links are preserved as content requires.

> 要进一步加强农业基础设施建设，切实做好防汛抗旱工作，努力实现粮食稳产增产。

We should further strengthen agricultural infrastructure development, ensure effective flood control and drought relief, and work to stabilize and increase grain output.

This example retains further development and the effort to achieve stable, increased output, using three parallel predicates. A short explanatory note accompanies actual delivery only when a register choice or evidence gap affects interpretation.

## Mechanical scanning and validation

```bash
python3 scripts/chinglish_scan.py "article 翻译(汉英对照).md"
python3 scripts/chinglish_scan.py "article 翻译(全英文).md" --plain
```

Run these commands from the repository, or use the script’s actual path. By default, the scanner skips source blockquotes, common code structures, and link destinations while inspecting English prose and pipe-table cells. `--plain` includes English blockquotes and every table column. Columns explicitly headed 中文, 原文, or Chinese are skipped by default.

The scanner reports candidates involving Chinese punctuation, verb phrases, noun density, and modifier attachment. It neither edits files nor verifies translation fidelity. English curly quotes, apostrophes, ellipses, and en/em dashes are valid punctuation. Complex nested Markdown, HTML, and formulas still require human review. Successful scans exit with code 0; invalid arguments or unreadable inputs exit with code 2.

Maintainers can run the mechanical regression suite:

```bash
python3 -m unittest discover -s scripts -p 'test_*.py' -v
```

[test-prompts.json](./test-prompts.json) contains trigger, exclusion, boundary, and semantic quality cases with a separate evaluation protocol. These support future model evaluation; passing script tests does not demonstrate translation quality.

## Repository contents

| File | Purpose |
|---|---|
| [SKILL.md](./SKILL.md) | Skill entry point, workflow, and delivery contract |
| [reference/techniques.md](./reference/techniques.md) | Structural methods, 16 transformation patterns, and candidate expressions |
| [reference/chinglish-symptoms.md](./reference/chinglish-symptoms.md) | Expression diagnostics, examples, and boundaries |
| [reference/text-analysis-and-qa.md](./reference/text-analysis-and-qa.md) | Register choices and accuracy checks |
| [reference/wordlists.md](./reference/wordlists.md) | Manual review lists; the scanner covers a subset of candidate patterns |
| [scripts/chinglish_scan.py](./scripts/chinglish_scan.py) | Read-only advisory scanner |
| [scripts/test_chinglish_scan.py](./scripts/test_chinglish_scan.py) | Scanner regression tests |
| [test-prompts.json](./test-prompts.json) | Trigger and quality evaluation cases |

For the reverse direction, see the sister skill [en-zh-translation-polish](https://github.com/HoraceLuBFA/en-zh-translation-polish).

## Credits and license

The code, prompts, and organization are released under the [MIT License](./LICENSE). The methods draw on Joan Pinkham’s *The Translator’s Guide to Chinglish* (Foreign Language Teaching and Research Press, 2000) and Lu Guoqiang’s *汉译英常用表达式经典惯例* (Shanghai Foreign Language Education Press, 2012). Reference tables are teaching adaptations for this skill and do not replace the books; rights to the original works and quotations remain with their respective holders. Thanks to [cangjie-skill](https://github.com/kangarooking/cangjie-skill) for its tools for organizing methods from books.

## Versions

Current version: [v1.1.1](https://github.com/HoraceLuBFA/zh-en-translation-polish/releases/tag/v1.1.1). See [CHANGELOG.md](./CHANGELOG.md) for changes and [Releases](https://github.com/HoraceLuBFA/zh-en-translation-polish/releases) for published versions.
