#!/usr/bin/env python3
"""Chinglish 机械扫描：对汉英对照 markdown 的英文行（非 `> ` 行）逐项报警。

用法: python3 chinglish_scan.py <file.md> [--plain]
  --plain  输入是纯英文文件（不跳过 blockquote 行）

输出为候选警告，不自动改写——每条要么改掉，要么译者能说出保留理由
（术语 / 政治定式 / hedging / 引文）。退出码始终为 0。
"""
import re
import sys

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

FULLWIDTH = re.compile(r"[，。：；？！（）【】《》、“”‘’…—　]")

DANGLER_STARTS = [
    (r"^\s*Based on\b", "based on 不在垂悬白名单 → On the basis of / In light of / Having studied"),
    (r"^\s*With (?:the|a|an|its|their|his|her) (?:[a-z]+ ){0,2}[a-z]+(?:ing|ment|tion|sion|ase|th)\b",
     "句首 With+抽象名词（「随着」？）→ When / Because / Thanks to，或拆句"),
    (r"^\s*Through (?:the )?\w+ing\b", "句首 Through+动名词 → 核对隐含主语是否=主句主语"),
    (r"^\s*In order to serve\b", "in order to serve you better 类不豁免"),
]

# ---------- 扫描 ----------

def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?;:])\s+", text) if s.strip()]

def scan(lines, plain=False):
    warns = []          # (lineno, category, message)
    cliche_counts = {}
    word_total = 0

    for i, ln in enumerate(lines, 1):
        s = ln.strip()
        if not s or s == "---":
            continue
        if not plain and ln.lstrip().startswith(">"):
            continue  # 中文原文行
        if s.startswith("```") or s.startswith("|"):
            continue  # 代码块围栏与表格行（表格内多为对照材料）

        word_total += len(re.findall(r"[A-Za-z]+", s))

        # 1. 全角标点残留
        m = FULLWIDTH.findall(s)
        if m and re.search(r"[A-Za-z]{3}", s):
            warns.append((i, "全角标点", f"英文行含全角符号 {''.join(sorted(set(m)))}"))

        # 2. 空壳框架
        for pat in SHELL_FRAMES:
            for hit in re.finditer(pat, s, re.IGNORECASE):
                warns.append((i, "空壳框架", f"“{hit.group(0)}” → 试删或把真主谓提为主句"))

        # 3. 套语动词短语
        for pat in CLICHE_VERB_PHRASES:
            for hit in re.finditer(pat, s, re.IGNORECASE):
                warns.append((i, "套语短语", f"“{hit.group(0)}” → 判断三问；多数应删，动作直接做谓语"))

        # 4. 空动词结构
        for pat in EMPTY_VERB_PATTERNS:
            for hit in re.finditer(pat, s, re.IGNORECASE):
                warns.append((i, "空动词", f"“{hit.group(0)}” → 名词还原为谓语动词"))

        # 5. 介词框架
        for pat in PREP_FRAMES:
            for hit in re.finditer(pat, s, re.IGNORECASE):
                warns.append((i, "介词框架", f"“{hit.group(0)}” → 试换 because/when/if/by V-ing"))

        # 6. 抽象名词密度（按句）
        for sent in sentences(s):
            hits = ABSTRACT_SUFFIX.findall(sent)
            if len(hits) >= 3:
                warns.append((i, "名词密度", f"一句 {len(hits)} 个抽象名词（{', '.join(hits[:5])}…）→ 换动词/形容词"))

        # 7. 陈套副词计数
        for w in CLICHE_ADVERBS:
            n = len(re.findall(rf"\b{w}\b", s, re.IGNORECASE))
            if n:
                cliche_counts[w] = cliche_counts.get(w, 0) + n

        # 8. 可疑连接词 / 垂悬起句（按句首匹配，不只行首）
        for sent in sentences(s):
            for pat, msg in DANGLER_STARTS:
                if re.search(pat, sent):
                    warns.append((i, "垂悬/连词", msg))
        for hit in re.finditer(r"\bwhile\b", s, re.IGNORECASE):
            warns.append((i, "while", "替换测试：多于一种读法（时间/although/whereas/and）读得通即歧义"))

    return warns, cliche_counts, word_total


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    plain = "--plain" in sys.argv
    if not args:
        print(__doc__)
        sys.exit(0)
    path = args[0]
    lines = open(path, encoding="utf-8").read().split("\n")
    warns, cliches, words = scan(lines, plain)

    by_cat = {}
    for lineno, cat, msg in warns:
        by_cat.setdefault(cat, []).append((lineno, msg))

    print(f"== chinglish_scan: {path} ==")
    print(f"英文词数 ~{words}")
    for cat in sorted(by_cat):
        items = by_cat[cat]
        print(f"\n[{cat}] {len(items)} 条")
        for lineno, msg in items[:20]:
            print(f"  L{lineno}: {msg}")
        if len(items) > 20:
            print(f"  …另 {len(items)-20} 条")

    # 陈套副词密度：每页(≈400词) ≤2 的指标
    if cliches and words:
        print("\n[陈套副词密度]（指标：resolutely 类每页≈400词 ≤2 次）")
        for w, n in sorted(cliches.items(), key=lambda kv: -kv[1]):
            per_page = n / max(words / 400, 1e-9)
            flag = " ←超标" if per_page > 2 else ""
            print(f"  {w}: {n} 次 (~{per_page:.1f}/页){flag}")

    total = len(warns)
    print(f"\n警告合计: {total}（候选，非判决——每条要么改，要么说得出保留理由）")


if __name__ == "__main__":
    main()
