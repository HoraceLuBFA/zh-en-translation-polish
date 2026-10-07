<div align="center">

# zh-en-translation-polish · 汉译英翻译润色

### 把中文译成忠实、自然的英文，支持逐段汉英对照

[![License: MIT](https://img.shields.io/badge/License-MIT-f5c542.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/version-1.1.1-2ea44f.svg)](./SKILL.md)
[![Agent Skills](https://img.shields.io/badge/agent-skills-black.svg)](https://github.com/vercel-labs/skills)

**[English](./README.en.md) | 中文**

</div>

## 这项技能做什么

本技能用于中文译英文，以及对照中文原文润色已有英文译稿。它借鉴 Joan Pinkham《中式英语之鉴》的诊断方法和陆国强《汉译英常用表达式经典惯例》的结构组织方法，先理清意义与语义角色，再选择自然的英语表达，最后双向核对原文和译文。

忠实性适用于所有文体。润色保留原文的事实、数字、限定、逻辑、语气和意象，区分尝试与结果、可能与确定、时间先后与因果。简化表达以前，先确认意义已完整保留；自然度和简洁度都不能替代准确性。

## 适用场景与边界

| 场景 | 处理重点 |
|---|---|
| 公文、政论与政策说明 | 核对官方定译、政策范围、力度、目标与承诺 |
| 学术摘要、论文与技术文档 | 保留术语、证据范围、情态、数字和单位，按语境组织句法 |
| 商务信函与企业官网 | 保留礼貌、宣称和承诺的原有强度；文案改写按用户授权进行 |
| 新闻、采访与行业文章 | 逐段保留具体例子、发言者、标题与图注归属 |
| 演讲、散文与个人表达 | 保留有作用的重复、节奏、比喻和个人语气 |
| 已有英文译稿 | 结合中文检查遗漏、增译及表达问题，准确自然的部分可以保留 |

英译中、直接以英文写作的润色和单个词语查询不属于本技能的完整流程。中文源文缺失时，可以先检查英文表达，但无法据此确认翻译忠实度。摘要、节译、宣传改写等需求以用户明确指定的范围为准。

## 安装

通过 [skills CLI](https://github.com/vercel-labs/skills) 安装，按提示选择要使用的 agent：

```bash
npx skills add -g HoraceLuBFA/zh-en-translation-polish
```

也可以把仓库链接交给支持技能安装的 agent：

> 帮我安装这个 skill：https://github.com/HoraceLuBFA/zh-en-translation-polish

手动安装可克隆到共享技能目录；如该目录已存在，先检查现有内容：

```bash
git clone https://github.com/HoraceLuBFA/zh-en-translation-polish.git ~/.agents/skills/zh-en-translation-polish
```

安装后检查 `SKILL.md` 是否存在，并在宿主的技能列表中确认可用。手动克隆后的发现方式取决于宿主配置，文件存在本身不代表已经加载。技能可独立使用，无需安装其他翻译技能；机械扫描需要 Python 3，仅使用标准库。

## 使用方式

安装并启用后，可以直接提出自然语言请求，也可以在支持显式调用的宿主中点名 `zh-en-translation-polish`。请提供待译中文；润色译稿时最好同时提供中文与英文。

- “把这段中文译成自然英文，汉英对照：……”
- “把这份中文论文摘要译成英文，只要英文译文，保留所有限定条件。”
- “对照这份中文原文润色英文译稿，保留数字、术语和引文。”
- “完整翻译这篇采访，保留发言者、图注与段落顺序，保存到指定文件。”

短段落直接在聊天中交付，不强制生成文件或展示完整诊断过程。用户指定的纯英文、双语和目标文件优先，已有目标文件按要求更新。

PDF 或其他文档通过宿主当前可用的读取工具获取原文。正文、图注、公式、引文和参考文献按任务范围保留；无法可靠提取的部分会说明缺口，不能以推测补齐。

## 工作流程

| 阶段 | 内容 |
|---|---|
| 0 · 通读与语域判断 | 确认任务范围，识别主体、逻辑、并列项、标题与句子重点 |
| 1 · 组织初译 | 按意义选择英语结构，保留动作与角色，不为套框架补事实 |
| 2 · 表达诊断 | 按需检查冗余、名词化、修饰关系、平行、语序、连接词与指代 |
| 3 · 双向核查 | 从原文检查覆盖，从译文检查依据，单查情态、范围、数字和归属 |
| 4 · 机械扫描 | 对落盘译文运行候选扫描，人工判断每条提示 |
| 5 · 交付 | 按要求输出；需要全英文文件时，从已核查的对照文件派生 |

长文按章节、发言者或连续小段分批翻译并就地核对，合并后再检查顺序、缺段、术语和指代。篇幅、段落数、零警告及模型自述均不能证明语义合格，也不设压缩率目标。

## 文件格式与输出示例

全文或项目翻译默认使用 `<名称> 翻译(汉英对照).md`：每段中文作为 blockquote，紧接英文。按需提供的 `<名称> 翻译(全英文).md` 从已核查的对照文件机械派生，避免重复撰写造成两版差异。共享图片、表格、公式、代码和链接按内容保留。

> 要进一步加强农业基础设施建设，切实做好防汛抗旱工作，努力实现粮食稳产增产。

We should further strengthen agricultural infrastructure development, ensure effective flood control and drought relief, and work to stabilize and increase grain output.

这一示例保留了“进一步”“建设”和“努力实现”的意义，用三个平行谓语组织英文。实际交付只在文体取舍或证据缺口影响理解时附简短说明。

## 机械扫描与验证

```bash
python3 scripts/chinglish_scan.py "文章 翻译(汉英对照).md"
python3 scripts/chinglish_scan.py "文章 翻译(全英文).md" --plain
```

以上命令在仓库目录运行；其他位置请使用脚本的实际路径。默认跳过原文 blockquote、常见代码结构和链接地址，检查英文正文与管道表格单元格；`--plain` 包含英文 blockquote 和全部表格列。明确标为“中文”“原文”或 Chinese 的表格列默认跳过。

扫描只提供中文标点、动词短语、名词密度和修饰关系等候选提示，不修改文件，不验证翻译忠实度。英文弯引号、撇号、省略号及 en/em dash 均可合法使用。复杂嵌套 Markdown、HTML 和公式仍需人工核查。扫描成功时退出码为 0，无效参数或输入读取失败时为 2。

维护者可运行机械回归检查：

```bash
python3 -m unittest discover -s scripts -p 'test_*.py' -v
```

[test-prompts.json](./test-prompts.json) 包含触发、排除、边界与语义质量案例，以及独立的评估方法。案例用于后续模型评估；脚本测试通过不代表实际翻译质量已通过评测。

## 仓库内容

| 文件 | 用途 |
|---|---|
| [SKILL.md](./SKILL.md) | 技能入口、工作流与交付约定 |
| [reference/techniques.md](./reference/techniques.md) | 结构组织方法、16 个转换模式及候选表达 |
| [reference/chinglish-symptoms.md](./reference/chinglish-symptoms.md) | 表达诊断、例句与适用边界 |
| [reference/text-analysis-and-qa.md](./reference/text-analysis-and-qa.md) | 文体处理与准确性质检 |
| [reference/wordlists.md](./reference/wordlists.md) | 人工检查词表，脚本覆盖其中部分候选模式 |
| [scripts/chinglish_scan.py](./scripts/chinglish_scan.py) | 只读机械扫描 |
| [scripts/test_chinglish_scan.py](./scripts/test_chinglish_scan.py) | 扫描行为回归测试 |
| [test-prompts.json](./test-prompts.json) | 触发与质量评估案例 |

反方向翻译请参阅姊妹技能 [en-zh-translation-polish](https://github.com/HoraceLuBFA/en-zh-translation-polish)。

## 致谢与许可

代码、提示词与组织方式以 [MIT 许可](./LICENSE) 发布。方法参考 Joan Pinkham《中式英语之鉴》（外语教学与研究出版社，2000）与陆国强《汉译英常用表达式经典惯例》（上海外语教育出版社，2012）；参考表为本技能的教学整理与改写，不替代原著，原著及其引文的权利归相应权利人所有。感谢 [cangjie-skill](https://github.com/kangarooking/cangjie-skill) 提供的书籍方法整理工具。

## 版本

当前版本：[v1.1.1](https://github.com/HoraceLuBFA/zh-en-translation-polish/releases/tag/v1.1.1)。更新记录见 [CHANGELOG.md](./CHANGELOG.md)，各版本可在 [Releases](https://github.com/HoraceLuBFA/zh-en-translation-polish/releases) 查看。
