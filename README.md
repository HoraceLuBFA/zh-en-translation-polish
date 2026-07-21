<div align="center">

# zh-en-translation-polish · 汉译英翻译润色

### 把中文译成地道、无中式英语的英文，并产出逐段“汉英对照”

[![License: MIT](https://img.shields.io/badge/License-MIT-f5c542.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-2ea44f.svg)](./SKILL.md)
[![Agent Skills](https://img.shields.io/badge/agent-skills-black.svg)](https://github.com/vercel-labs/skills)

**[English](./README.en.md) | 中文**

</div>

---

## 翻译理念

本 skill 把两本互补经典的汉译英方法论，工程化为一条中译英流水线：

- **Joan Pinkham《中式英语之鉴》**——减法与诊断：十三类中式英语病症的识别与修法；
- **陆国强《汉译英常用表达式经典惯例》**——加法与构造：概念表达结构化，把汉语义群装进英语的结构框架。

核心信条来自 Pinkham：

> 中式英语不是语法错误，而是**语法全对、但英语母语者不会这么写**的英语；它的共同根源是**多余的词**——“Unnecessary words are the hallmark of Chinglish.”

据此，地道的译文应当做到四点：

- **先构造后诊断**——初译不逐词对应，而是切分汉语义群、找到英语的结构核心（动词＋名词＋介词的固定框架）、按语义角色入槽；
- **砍掉汉语迁移**——范畴词、套语前缀、四字对偶冗余、名词化堆叠、垂悬修饰语、缺失的逻辑连接词，逐条诊断修正；
- **双轨质检**——英文内部逻辑与中文原文回查并行。Pinkham 本人不懂中文、只能单轨；能读原文是本 skill 相对原书多出的一只眼，因此“删任何重复前必回原文”是强制步骤；
- **按文体收放**——政论用官方定译、学术保 hedging、企业外宣自称降格承诺收敛、文学删繁规则全面降档。

每一段译文都走完“定档标注 → 概念结构化初译 → 九步诊断 → 双轨质检 → 机械扫描 → 汉英对照”的完整闭环，逐段打磨之后再交付。

## 适用场景

- **消除中式英语**——make great efforts to、attach great importance to、万能 With、名词串灾难、句首垂悬……逐条识别并修正；
- **政论与公文外译**——套语三分法（引导套语删／中心谓语换地道表达）、官方定译优先、政治定式与领导人讲话的保留规则；
- **学术摘要与论文**——hedging 逐个保留不升格、动词强度阶梯（show < demonstrate < verify < confirm）、警惕术语升格增译；
- **企业官网与外宣**——自称降格（a leading company 而非 We lead this industry）、收益承诺收敛（合规视角）；
- **维护汉英对照**——以对照文件为单一真源，全英文版由脚本派生，两版始终一致。

## 润色边界

方法服务于译文。Pinkham 本人的立场比她的规则宽容得多，这一层丢了就成了无差别删词机：

- **可疑短语“四次里有一次真有意义”**——见到不是删，是判断：它在此语境被证成了吗？为句意所必需吗？还是只因汉语里有就搬进来了？
- **拿不准就两个都留**——正式文本“冒着保留冗余的风险，好过冒丢失原意的风险”（Sol Adler：*meaning must have priority over elegance*）；
- **修饰语五级处置刚性**——纯冗余可删；强调型可能因政治定式必须保留；弱化型可能是有意自谦（学术 hedging）必须保留；
- **不要为地道牺牲准确**——换词避重复必须语义等值。底线：**理解错误没有原谅的余地。**

## 工作流

按序执行，每段译文走完全部阶段后再交付。

| 阶段 | 名称 | 做什么 |
|---|---|---|
| 0 | 定档与通读标注 | 判定七类文体档位；中文侧预标逻辑关系、并列串词类、标题模板、句焦点 |
| 1 | 概念结构化初译 | 切义群 → 找结构核心 → 语义角色入槽 → 验证语义相容性 |
| 2 | 九步减法诊断 | 删冗余 → 消名词化 → 修垂悬 → 修平行 → 调语序 → 补连接词 → 修代词 → 读音 → 连锁自检 |
| 3 | 双轨质检 | 英文逻辑独立核 + 回查中文原文；压缩率 20–50% 自查 |
| 4 | 机械扫描 | 脚本报警：全角残留／空壳框架／套语／名词密度／句首 With·based on／while 歧义 |
| 5 | 输出汉英对照 | 逐段配对，附一句“档位判定 + 主要取舍说明” |

支撑工作流的四张参考表与一个脚本（位于 `reference/` 与 `scripts/`）：

- **`chinglish-symptoms.md`**——十三类病症：汉语触发条件 → 机械诊断 → 修法 → 判断边界；
- **`techniques.md`**——概念结构化四法 + 16 个汉英结构转换模式 + 高频概念结构备查；
- **`text-analysis-and-qa.md`**——七类文体打折表、边界红线、准确性质检清单；
- **`wordlists.md`**——汉语触发词表与英语警戒词表（与扫描脚本同步）；
- **`chinglish_scan.py`**——机械扫描，只报警不改写：警告是候选不是判决，每条要么改、要么说得出保留理由。

## 安装

**方式一 · 一行命令（推荐）**

```bash
npx skills add -g HoraceLuBFA/zh-en-translation-polish
```

> [`npx skills`](https://github.com/vercel-labs/skills) 会把 skill 安装到 `~/.agents/skills/`——多个 agent 共用的 skill 目录，并自动建好各 agent 所需的软链。

**方式二 · 交给 agent 安装**

把仓库链接发给你的编码 agent（Claude Code / Codex / Gemini CLI 等），一句“帮我安装这个 skill”即可：

> 帮我安装这个 skill：https://github.com/HoraceLuBFA/zh-en-translation-polish

**方式三 · 手动 clone**

```bash
git clone https://github.com/HoraceLuBFA/zh-en-translation-polish.git ~/.agents/skills/zh-en-translation-polish
```

安装后验证：

```bash
test -f ~/.agents/skills/zh-en-translation-polish/SKILL.md && echo OK
```

## 使用方式

**自然语言**——直接提出需求即可，支持自动触发的 agent 会据 `SKILL.md` 的 `description` 字段加载本 skill。常见说法：

- “把这段中文翻译成英文，要地道，别有中式英语味：……”
- “帮我把这个论文摘要翻成英文投期刊，中英对照。”
- “同事翻的这版英文有点 Chinglish，帮我润一润。”

**命令显式调用**——直接点名本 skill，把文件或文本作为参数传入：

```text
# Claude Code：斜杠命令
/zh-en-translation-polish path/to/document.md

# Codex：用 $ 显式调用（或先 /skills 从列表选择）
$zh-en-translation-polish path/to/document.md
```

> ⚠️ **想要纯英文输出**：本 skill **默认产出汉英对照**。若只要英文译文，请在 prompt 里显式强调，例如“只要英文，不要中文对照”——否则会默认给对照版。

## 交付物

1. **`<名称> 翻译(汉英对照).md`**——单一真源：每段中文原文作为 blockquote，其下紧接英文译文；
2. **`<名称> 翻译(全英文).md`**（按需）——由脚本从对照文件派生；
3. 一段简短说明——交代本篇的文体档位判定与主要取舍。

## 输出预览

> 要进一步加强农业基础设施建设，切实做好防汛抗旱工作，努力实现粮食稳产增产。

We should strengthen agricultural infrastructure, ensure effective flood control and drought relief, and keep grain output stable and growing.

*（档位判定：政论／公文，官方定译优先；「建设」范畴词脱落，「切实做好／努力实现」套语处理，「防汛抗旱」用定译 flood control and drought relief。）*

## 姊妹 skill

反方向（英→中）请用 **[en-zh-translation-polish](https://github.com/HoraceLuBFA/en-zh-translation-polish)**——蒸馏自叶子南《高级英汉翻译理论与实践》，把英文译成地道、无翻译腔的中文，并产出英中对照。两个 skill 结构对称、互为镜像，各管一个方向。

## 仓库结构

```text
zh-en-translation-polish/
├── SKILL.md                       # 主入口（工作流 + 派生脚本）
├── README.md                      # 项目说明（面向人）
├── reference/
│   ├── chinglish-symptoms.md      # 十三类中式英语病症诊断
│   ├── techniques.md              # 概念结构化 + 16 个转换模式
│   ├── text-analysis-and-qa.md    # 文体打折表 + 边界红线 + 质检清单
│   └── wordlists.md               # 触发词表 + 警戒词表
├── scripts/
│   └── chinglish_scan.py          # 机械扫描（advisory）
├── test-prompts.json              # 触发／诱饵／边界测试用例
├── LICENSE
└── .gitignore
```

## 致谢与许可

本 skill 的代码、提示词与组织方式以 **MIT 许可**发布，可自由使用、修改、再分发，详见 [LICENSE](./LICENSE)。

方法论与判例蒸馏、转述自 **Joan Pinkham《中式英语之鉴（The Translator's Guide to Chinglish）》（外语教学与研究出版社，2000）** 与 **陆国强《汉译英常用表达式经典惯例》（上海外语教育出版社）**，在此谨致谢忱。`reference/` 中的少量引文系评注与教学目的的简短摘引，著作权归原作者与出版社所有；本 skill 仅为方法工具，不能替代原著，建议系统学习者购买正版。

本 skill 借助 [cangjie-skill](https://github.com/kangarooking/cangjie-skill)（将书籍方法论蒸馏为可调用 AI skill 的开源拆书流水线）生成，一并致谢。
