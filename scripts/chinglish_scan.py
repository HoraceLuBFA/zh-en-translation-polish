#!/usr/bin/env python3
"""Scan English prose in bilingual Markdown for review candidates.

No automatic edits or fidelity verdict. Successful scans exit 0 regardless of
warnings; invalid arguments or unreadable inputs exit 2. Uses Python 3 stdlib.
"""
import re

# ---------- 词表（与 reference/wordlists.md 同步） ----------

SHELL_FRAMES = [
    r"\bthe fact that\b", r"\bthe situation in which\b", r"\ba situation where\b",
    r"\bthis state of affairs\b", r"\blies in the fact\b", r"\bthe key to \w+ lies in\b",
    r"\bis a subject that\b", r"\bconstitutes? a period in which\b",
    r"\bin the field of\b", r"\bin the sphere of\b", r"\bthe work of\b",
    r"\bthe practice of\b", r"\bthe phenomenon (?:of|that)\b",
]

CLICHE_VERB_PHRASES = [
    r"\bmake (?:great|every|active|vigorous) efforts? to\b", r"\bexert (?:great )?efforts? to\b",
    r"\bmake efforts? to\b", r"\btry (?:our|their|its) best to\b", r"\bdo (?:our|their|its) utmost to\b",
    r"\bpay (?:close |great |high )?attention to\b", r"\bpay heed to\b",
    r"\battach (?:great |high )?importance to\b", r"\blay stress on\b",
    r"\bdo a good job (?:in|of)\b", r"\bmake a success of\b",
    r"\btake (?:effective |active |vigorous )?measures to\b", r"\btake steps to\b",
    r"\bgive full (?:play|scope) to\b", r"\bplay an? (?:\w+ )?role in\b",
    r"\bis of great significance\b",
]

EMPTY_VERB_PATTERNS = [
    r"\bmake an? \w+(?:ment|tion|sion|ance|ysis) (?:of|in|to)\b",
    r"\bconduct an? \w+ of\b", r"\bcarry out the \w+ of\b",
    r"\bgive guidance to\b", r"\bprovide assistance to\b",
    r"\bexercise control over\b", r"\bregister(?:ed)? an? (?:increase|decrease)\b",
    r"\bplace stress on\b", r"\bachieve success in\b",
    r"\bbring about an? \w+\b", r"\baccomplish the \w+ of\b",
    r"\brealize the \w+ of\b",
]

PREP_FRAMES = [
    r"\bdue to\b", r"\bowing to\b", r"\bas a result of\b", r"\bresult(?:ed|ing)? from\b",
    r"\bin the course of\b", r"\bfor the purpose of\b", r"\bin the process of\b",
    r"\bby means of\b", r"\bon the basis of\b", r"\black of\b", r"\bshortage of\b",
    r"\babsence of\b", r"\bin terms of\b", r"\bwith regard to\b",
]

CLICHE_ADVERBS = [
    "resolutely", "unswervingly", "vigorously", "conscientiously", "energetically",
    "persistently", "unremittingly", "diligently", "actively", "effectively",
    "successfully", "thoroughly", "firmly",
]

ABSTRACT_SUFFIX = re.compile(
    r"\b[a-z]{3,}(?:tion|sion|ment|ance|ence|ity|ness|ship|ancy)s?\b", re.IGNORECASE)

# English curly quotes, apostrophes, ellipses and dashes are valid punctuation.
FULLWIDTH = re.compile(r"[，。：；？！（）【】《》、　]")

DANGLER_STARTS = [
    (r"^\s*With (?:the|a|an|its|their|his|her) (?:[a-z]+ ){0,2}[a-z]+(?:ing|ment|tion|sion|ase|th)\b",
     "句首 With 结构：核对修饰关系与源文逻辑；合法的伴随或背景表达可保留"),
    (r"^\s*Through (?:the )?\w+ing\b", "句首 Through 结构：核对动作主体与修饰对象"),
    (r"^\s*In order to serve\b", "目的不定式：核对动作主体与所属小句是否相容"),
]

# ---------- Bounded Markdown prose extraction ----------

def _blank(match):
    """Mask syntax without changing source line numbers."""
    return re.sub(r"[^\n]", " ", match.group(0))


def _inline_code(text):
    # Match equal-length backtick runs, including spans across lines. Unclosed
    # runs are literal Markdown and must not swallow subsequent prose.
    parts = list(re.finditer(r"`+", text))
    chars = list(text)
    i = 0
    while i < len(parts):
        opener = parts[i]
        end = next((j for j in range(i + 1, len(parts))
                    if len(parts[j].group()) == len(opener.group())), None)
        if end is None:
            i += 1
            continue
        for pos in range(opener.start(), parts[end].end()):
            if chars[pos] != "\n":
                chars[pos] = " "
        i = end + 1
    return "".join(chars)


def _visible_links(text):
    # Keep visible labels/alt text, mask destinations (including balanced
    # parentheses and optional titles). This is not a full CommonMark parser.
    pattern = re.compile(r"!?\[([^\[\]]*)\]\(")
    while True:
        match = pattern.search(text)
        if not match:
            break
        depth, pos = 1, match.end()
        while pos < len(text) and depth:
            if text[pos] == "\\":
                pos += 2
                continue
            if text[pos] == "(":
                depth += 1
            elif text[pos] == ")":
                depth -= 1
            pos += 1
        if depth:
            break
        text = text[:match.start()] + match.group(1) + " " + text[pos:]
    text = re.sub(r"!?\[([^\[\]]+)\]\[[^\]]*\]", r"\1", text)
    text = re.sub(r"<(?:https?://|mailto:)[^>]+>", " ", text, flags=re.I)
    text = re.sub(r"(?:https?://|www\.)[^\s<>]+", " ", text, flags=re.I)
    return text


def _cells(line):
    value = line.strip()
    if value.startswith("|"):
        value = value[1:]
    if value.endswith("|") and not value.endswith(r"\|"):
        value = value[:-1]
    return [part.replace(r"\|", "|").strip()
            for part in re.split(r"(?<!\\)\|", value)]


def _separator(line):
    cells = _cells(line)
    return len(cells) > 1 and all(re.fullmatch(r":?-{3,}:?", c) for c in cells)


def iter_prose_fragments(lines, plain=False):
    """Yield (original line number, prose fragment); table cells stay separate.

    Handles ordinary fenced/indented code, front matter, comments, inline code,
    links and pipe tables. Deeply nested Markdown/HTML and math syntax require
    human review. Default blockquotes contain Chinese source and are excluded.
    """
    lines = list(lines)
    masked = [line.rstrip("\r\n") for line in lines]
    if masked and masked[0].strip() == "---":
        end = next((i for i in range(1, len(masked))
                    if masked[i].strip() in ("---", "...")), None)
        if end is not None:
            masked[:end + 1] = [""] * (end + 1)
    fence = None
    list_indent = None
    for i, line in enumerate(masked):
        if not plain and line.lstrip().startswith(">"):
            masked[i] = ""
            continue
        if plain:
            line = re.sub(r"^\s*(?:> ?)+", "", line)
        if fence:
            char, size = fence
            if re.fullmatch(r" {0,3}" + re.escape(char) + "{" + str(size) + r",}\s*", line):
                fence = None
            masked[i] = ""
            continue
        opening = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if opening and (opening[1][0] != "`" or "`" not in opening[2]):
            fence = (opening[1][0], len(opening[1]))
            masked[i] = ""
            continue
        marker = re.match(r"^( *)(?:[-+*]|\d+[.)]) +", line)
        indent = len(line) - len(line.lstrip(" "))
        if marker:
            list_indent = marker.end()
        elif line.strip() and (list_indent is None or indent < list_indent):
            list_indent = None
        if (line.startswith("\t") or indent >= 4) and list_indent is None:
            masked[i] = ""
            continue
        if re.match(r"^ {0,3}\[[^\]]+\]:\s*", line):
            masked[i] = ""
            continue
        masked[i] = line
    # Code can display literal comment delimiters. Mask code first so an
    # unclosed HTML example cannot hide the prose that follows it.
    masked = re.sub(r"<!--.*?(?:-->|\Z)", _blank,
                    _inline_code("\n".join(masked)), flags=re.S).split("\n")
    source_columns = set()
    in_table = False
    for i, line in enumerate(masked):
        line = _visible_links(line)
        if not line.strip():
            in_table = False
            continue
        if _separator(line):
            continue
        is_header = i + 1 < len(masked) and _separator(masked[i + 1])
        if is_header:
            in_table = True
            source_columns = {j for j, cell in enumerate(_cells(line))
                              if cell.strip(" *").lower() in
                              ("中文", "原文", "中文原文", "chinese", "source (chinese)")}
        if in_table and re.search(r"(?<!\\)\|", line):
            for j, cell in enumerate(_cells(line)):
                if j not in source_columns or plain:
                    yield i + 1, cell
        else:
            in_table = False
            # Strip list and heading markers before sentence-start rules.
            line = re.sub(r"^\s*(?:#{1,6}\s+|[-+*]\s+|\d+[.)]\s+)", "", line)
            if line.strip() and not re.fullmatch(r"\s*[-*_]{3,}\s*", line):
                yield i + 1, line


# ---------- Candidate diagnostics ----------

def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?;:])\s+", text) if s.strip()]


def scan(lines, plain=False):
    warns, cliche_counts, word_total = [], {}, 0
    rules = [
        (SHELL_FRAMES, "结构候选", "核对是否有独立意义；确认等值后才简化"),
        (CLICHE_VERB_PHRASES, "动词短语", "核对尝试、程度、优先级和目标；不得直接删成结果"),
        (EMPTY_VERB_PATTERNS, "名词化表达", "可比较动词表达，保留角色、范围和完成状态"),
        (PREP_FRAMES, "介词框架", "核对可读性与原有关系；不因改写补入因果或条件"),
    ]
    for i, s in iter_prose_fragments(lines, plain):
        word_total += len(re.findall(r"[A-Za-z]+", s))
        marks = FULLWIDTH.findall(s)
        if marks and re.search(r"[A-Za-z]{3}", s):
            warns.append((i, "中文标点", f"英文片段含中文符号 {''.join(sorted(set(marks)))}；核对是否为专名或原文内容"))
        for patterns, category, advice in rules:
            for pattern in patterns:
                for hit in re.finditer(pattern, s, re.I):
                    warns.append((i, category, f"“{hit.group(0)}”：{advice}"))
        for sent in sentences(s):
            hits = ABSTRACT_SUFFIX.findall(sent)
            if len(hits) >= 3:
                warns.append((i, "名词密度", f"片段含 {len(hits)} 个后缀候选（{', '.join(hits[:5])}）；检查可读性，术语和自然表达可保留"))
            for pattern, advice in DANGLER_STARTS:
                if re.search(pattern, sent, re.I):
                    warns.append((i, "修饰关系", advice))
        for word in CLICHE_ADVERBS:
            count = len(re.findall(rf"\b{word}\b", s, re.I))
            if count:
                cliche_counts[word] = cliche_counts.get(word, 0) + count
    return warns, cliche_counts, word_total


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="UTF-8 Markdown or plain text file")
    parser.add_argument("--plain", action="store_true", help="include English blockquotes and all table columns")
    args = parser.parse_args()
    try:
        lines = open(args.path, encoding="utf-8").read().splitlines()
    except (OSError, UnicodeError) as exc:
        parser.exit(2, f"Cannot read input: {exc}\n")
    warns, cliches, words = scan(lines, args.plain)
    by_cat = {}
    for lineno, category, message in warns:
        by_cat.setdefault(category, []).append((lineno, message))
    print(f"== chinglish_scan: {args.path} ==")
    print(f"英文词数估计 ~{words}（已排除识别出的代码和链接地址）")
    for category in sorted(by_cat):
        items = by_cat[category]
        print(f"\n[{category}] {len(items)} 条")
        for lineno, message in items[:20]:
            print(f"  L{lineno}: {message}")
        if len(items) > 20:
            print(f"  …另 {len(items) - 20} 条")
    if cliches:
        print("\n[副词次数]（供核对分布与语义，不设删除阈值）")
        for word, count in sorted(cliches.items(), key=lambda kv: (-kv[1], kv[0])):
            print(f"  {word}: {count} 次")
    print(f"\n候选警告合计: {len(warns)}；允许有依据地保留。")
    print("本工具不验证翻译忠实度；零警告不代表语义核查通过。")


if __name__ == "__main__":
    main()
