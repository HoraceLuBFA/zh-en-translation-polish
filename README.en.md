<div align="center">

# zh-en-translation-polish

### Translate Chinese into idiomatic, Chinglish-free English, with paragraph-by-paragraph bilingual output

[![License: MIT](https://img.shields.io/badge/License-MIT-f5c542.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-2ea44f.svg)](./SKILL.md)
[![Agent Skills](https://img.shields.io/badge/agent-skills-black.svg)](https://github.com/vercel-labs/skills)

**English | [中文](./README.md)**

</div>

---

## Philosophy

This skill turns the Chinese-to-English methodology of two complementary classics into an executable pipeline:

- **Joan Pinkham, *The Translator's Guide to Chinglish*** — subtraction and diagnosis: how to recognize and fix thirteen families of Chinglish symptoms;
- **Lu Guoqiang, *Classic Examples of Converting Chinese to English*** — addition and construction: conceptual structurization, fitting Chinese sense groups into English structural frames.

The core conviction comes from Pinkham:

> Chinglish is not ungrammatical English — it is English that is grammatically correct **but that no educated native speaker would write**. Its common root is surplus words: *"Unnecessary words are the hallmark of Chinglish."*

Good translation therefore rests on four principles:

- **Construct first, then diagnose** — the draft is not word-for-word mapping but slot-filling: segment the Chinese sense groups, find the English structural core (a fixed verb + noun + preposition frame), assign each group to its semantic slot;
- **Cut what Chinese smuggles in** — category nouns, exhortation boilerplate, redundant four-character twins, noun plagues, dangling modifiers, and missing logical connectives, fixed one symptom at a time;
- **Dual-track QA** — check the English on its own internal logic *and* against the Chinese source. Pinkham herself read little Chinese and could only run one track; reading the source is this skill's extra eye, so "consult the original before deleting any 'redundancy'" is mandatory;
- **Tune to the register** — official canonical renderings for policy text, hedging preserved for academic prose, self-claims downgraded and promises softened for corporate copy, deletion rules demoted to suggestions for literature.

Every paragraph runs the full loop — *register & annotation → structurized draft → nine-step diagnosis → dual-track QA → mechanical scan → bilingual output* — and is polished before it ships.

## What it is for

- **De-Chinglishing** — *make great efforts to*, *attach great importance to*, universal *With*, noun-string pileups, sentence-initial danglers: each detected and repaired;
- **Policy and government text** — a three-way rule for boilerplate (delete lead-ins, re-express central predicates idiomatically), canonical official renderings first, preservation rules for set political phrases;
- **Academic abstracts and papers** — hedges preserved one-for-one, a verb-strength ladder (show < demonstrate < verify < confirm), guard against covert term upgrades (小样本 → *few-shot*);
- **Corporate websites** — self-claims downgraded (*a leading company*, not *We lead this industry*), return promises converged into value commitments (a compliance concern);
- **Maintaining bilingual documents** — the side-by-side file is the single source of truth; the English-only version is derived by script, so the two never drift.

## Boundaries

Pinkham herself was far more permissive than her rules; drop this layer and the skill becomes an indiscriminate word-deleter:

- **A suspect phrase "is mere padding three times out of four — the fourth time it carries meaning."** Seeing one triggers judgment, not deletion;
- **When in doubt, keep both** — in formal documents "it is better to risk including a redundancy than to risk losing an element of the intended sense" (Sol Adler: *meaning must have priority over elegance*);
- **Five grades of modifier rigidity** — pure redundancies may be cut on sight; intensifiers may be fixed political formulas that must stay; qualifiers may be deliberate modesty (or academic hedging) that must stay;
- **Never trade accuracy for idiom** — synonym substitution must preserve meaning. Bottom line: **a comprehension error has no excuse.**

## Workflow

Executed in order; every paragraph completes all stages before delivery.

| Stage | Name | What happens |
|---|---|---|
| 0 | Register & annotation | Pick one of seven registers; pre-mark logical relations, list word-classes, heading templates, and sentence focus on the Chinese side |
| 1 | Structurized draft | Segment sense groups → find the structural core → fill semantic slots → verify semantic compatibility |
| 2 | Nine-step diagnosis | Cut surplus words → kill nominalization → fix danglers → fix parallelism → reorder for end-focus → add connectives → fix pronouns → read aloud → cascade check |
| 3 | Dual-track QA | Independent English-logic pass + line-by-line check against the Chinese; 20–50% compression self-check |
| 4 | Mechanical scan | Script flags full-width punctuation, shell frames, boilerplate, abstract-noun density, sentence-initial *With* / *based on*, ambiguous *while* |
| 5 | Bilingual output | Paragraph-paired file plus a one-line note on register ruling and key trade-offs |

Four reference tables and one script support the workflow (`reference/`, `scripts/`):

- **`chinglish-symptoms.md`** — thirteen symptom families: Chinese trigger → mechanical test → fix → judgment boundary;
- **`techniques.md`** — four construction methods + 16 Chinese-to-English structural transformation patterns + a quick-reference of high-frequency conceptual structures;
- **`text-analysis-and-qa.md`** — the seven-register discount table, red lines, and the accuracy QA checklist;
- **`wordlists.md`** — Chinese trigger words and English warning words (kept in sync with the scanner);
- **`chinglish_scan.py`** — advisory scanner: warnings are candidates, not verdicts — each one is either fixed or retained with a stated reason.

## Installation

**Option 1 · One-liner (recommended)**

```bash
npx skills add -g HoraceLuBFA/zh-en-translation-polish
```

> [`npx skills`](https://github.com/vercel-labs/skills) installs into `~/.agents/skills/` — the shared skills directory — and sets up the symlinks each agent needs.

**Option 2 · Let your agent install it**

Send the repo link to your coding agent (Claude Code / Codex / Gemini CLI, etc.):

> Install this skill for me: https://github.com/HoraceLuBFA/zh-en-translation-polish

**Option 3 · Manual clone**

```bash
git clone https://github.com/HoraceLuBFA/zh-en-translation-polish.git ~/.agents/skills/zh-en-translation-polish
```

Verify:

```bash
test -f ~/.agents/skills/zh-en-translation-polish/SKILL.md && echo OK
```

## Usage

**Natural language** — just ask; agents with auto-triggering load the skill from the `description` field:

- "把这段中文翻译成英文，要地道，别有中式英语味……"
- "Translate this Chinese abstract into English for journal submission, bilingual please."
- "This English draft my colleague translated reads Chinglish — polish it."

**Explicit invocation**:

```text
# Claude Code: slash command
/zh-en-translation-polish path/to/document.md

# Codex: invoke with $ (or pick from /skills)
$zh-en-translation-polish path/to/document.md
```

> ⚠️ **English-only output**: this skill produces a **Chinese-English side-by-side file by default**. If you want the English only, say so explicitly — e.g. "English only, no bilingual pairing".

## Deliverables

1. **`<name> 翻译(汉英对照).md`** — single source of truth: each Chinese paragraph as a blockquote, followed by its English translation;
2. **`<name> 翻译(全英文).md`** (on request) — derived from the bilingual file by script;
3. A short note stating the register ruling and the main trade-offs.

## Preview

> 要进一步加强农业基础设施建设，切实做好防汛抗旱工作，努力实现粮食稳产增产。

We should strengthen agricultural infrastructure, ensure effective flood control and drought relief, and keep grain output stable and growing.

*(Register: policy/official — canonical renderings first; the category noun 「建设」 dropped, boilerplate 「切实做好／努力实现」 resolved, 「防汛抗旱」 rendered with the canonical* flood control and drought relief*.)*

## Sister skill

For the opposite direction (English → Chinese), use **[en-zh-translation-polish](https://github.com/HoraceLuBFA/en-zh-translation-polish)** — distilled from Ye Zinan's *Advanced Course in English-Chinese Translation*, it produces idiomatic, translationese-free Chinese with bilingual pairing. The two skills are structural mirrors, one per direction.

## Repository layout

```text
zh-en-translation-polish/
├── SKILL.md                       # Main entry (workflow + derivation script)
├── README.md                      # Project readme (for humans)
├── reference/
│   ├── chinglish-symptoms.md      # Thirteen Chinglish symptom families
│   ├── techniques.md              # Conceptual structurization + 16 patterns
│   ├── text-analysis-and-qa.md    # Register discounts + red lines + QA checklist
│   └── wordlists.md               # Trigger words + warning words
├── scripts/
│   └── chinglish_scan.py          # Mechanical scanner (advisory)
├── test-prompts.json              # Trigger / decoy / edge-case tests
├── LICENSE
└── .gitignore
```

## Acknowledgements & License

Code, prompts, and organization are released under the **MIT License** — see [LICENSE](./LICENSE).

The methodology and exemplars are distilled and paraphrased from **Joan Pinkham, *The Translator's Guide to Chinglish*** (Foreign Language Teaching and Research Press, 2000) and **Lu Guoqiang, *Classic Examples of Converting Chinese to English in Terms of Expressions for Everyday Use*** (Shanghai Foreign Language Education Press, 2012), with gratitude. The brief quotations in `reference/` are short excerpts for commentary and teaching; copyright remains with the original authors and publishers. This skill is a method tool, not a substitute for the books — buy them if you want the full course.

Built with [cangjie-skill](https://github.com/kangarooking/cangjie-skill), an open-source pipeline that distills book methodologies into callable AI skills — thanks as well.
