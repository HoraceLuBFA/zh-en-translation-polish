---
name: zh-en-translation-polish
description: >-
  Translates Chinese into idiomatic, Chinglish-free English, optionally as a
  Chinese-English bilingual version pairing each source paragraph with its
  translation. Use whenever the user wants to 翻译成英文 / 汉译英 / 中译英,
  去中式英语 (de-Chinglish an English draft translated from Chinese), or
  produce a 汉英对照 bilingual rendering — company profiles, policy or
  government text, academic abstracts, speeches, marketing copy, everyday
  documents. Trigger even on casual phrasing like "把这段翻成英文" or
  "帮我把这个翻译润色一下 (into English)". Not for English-to-Chinese
  (use en-zh-translation-polish), pure English writing unrelated to a
  Chinese source, or single-word lookups.
license: MIT
version: 1.0.0
tags: [translation, english, chinese-to-english, 汉译英, 中式英语, 润色, 汉英对照]
allowed-tools: Read Write Edit Bash
---

# 汉译英翻译润色 (Chinese→English Translate & Polish)

把中文译成**地道英文**并产出**汉英对照**译文。核心信条（Pinkham《中式英语之鉴》+ 陆国强《汉译英常用表达式经典惯例》）：Chinglish 不是语法错误，是**语法全对但母语者不会这么写**的英语；判定标准不是对错而是像不像。它的共同根源是**多余的词**（"Unnecessary words are the hallmark of Chinglish"）。好译文 = **先构造后诊断**——初译用「概念结构化」把汉语义群装进英语结构框架，润色用九步流水线砍掉汉语迁移进来的冗余与错位；全程**双轨质检**（英文逻辑 + 回查中文），这是我们比只懂英文的润色者多出的一只眼。

## 交付物

默认产出**一个**汉英对照 Markdown 文件；用户要「全英文版」时再脚本派生。

1. **`<名称> 翻译(汉英对照).md`** — 唯一真源。每段**中文原文作为 blockquote (`> `)**，紧跟其下是英文译文。
2. （按需）**`<名称> 翻译(全英文).md`** — 脱离对照文件**用脚本机械派生**（删掉 `> ` 行），不要重打英文。
   ```bash
   python3 - "<名称> 翻译(汉英对照).md" "<名称> 翻译(全英文).md" <<'PY'
   import sys, re
   src, dst = sys.argv[1], sys.argv[2]
   lines = open(src, encoding='utf-8').read().split('\n')
   kept = [ln for ln in lines if not ln.lstrip().startswith('>')]
   open(dst,'w',encoding='utf-8').write(re.sub(r'\n{3,}','\n\n','\n'.join(kept)).strip()+'\n')
   PY
   ```
   > 顺序要求：**先跑阶段 6 的机械扫描并清零问题，再派生全英文版**——派生脚本原样继承文本，不会再纠正。

若输入只是聊天里的一小段（几句话），直接在回复里给对照即可，不必落盘；成篇文章或用户指明保存才写文件。命名沿用源文件名，无工具前缀（除非用户要）。目标文件已存在则更新而非新建。

## 工作流（严格按序；每段译文都要走完诊断，不是初译就交）

### 阶段 0 — 定档与通读标注 ★必做第一步

**A. 文体定档**：判定文体类型与规则打折档位，详见 `reference/text-analysis-and-qa.md` 小节 A。一句话档位写进给用户的说明里。

- **政论/外宣/公文**：Pinkham 全套规则火力全开（她的语料就是这类），但注意政治定式、领导人讲话的保留规则，以及**官方定译优先**（防汛抗旱 → flood control and drought relief，不自由意译）。
- **技术文档**：术语固化优先于拆名词串；含混处向用户提问而非擅自推定。
- **学术论文**：★弱化词（qualifiers）是必需的 hedging，**不删**；动词强度不升格（验证→demonstrate 不到 confirm）；警惕术语升格增译（小样本→few-shot）；被动语态在方法部分是惯例，不强改主动。
- **商务信函**：寒暄与缓冲承载关系信息，不按「空话」删除。
- **企业外宣/官网**：自称降格（a leading company，不写 We lead this industry）、收益承诺收敛（合规），原文的过度宣称按英文语体收敛不放大。
- **口语/演讲稿**：听众不能回读——短主句、前置主干，允许适度重复；不机械尾重。
- **文学/散文**：折扣最大。排比、复沓、有意的冗余是修辞建构手段，删繁规则全部降为「建议」。

**B. 中文侧标注**（动笔前在原文上做，返工量减半）：

1. **逻辑关系**：标注每对相邻分句的关系（因果/转折/让步/递进/条件/例证）。汉语意合，这些关系不在字面上，不先读出来英译必漏。
2. **并列串**：为每个顿号/「和」串**预先决定英文统一词类**。中文并列靠语义同类成立，英语要语法+语义双重同类。
3. **小标题**：把全文同级标题抽成一列，**先定模板再翻第一条**（汉语动宾式标题首选 gerund，其次 infinitive）。
4. **句焦点**：判定每句的核心断言（决定阶段 4 的语序）。焦点取决于上下文，不是单句。

### 阶段 1 — 概念结构化初译（构造，不是逐词对应）

汉语一句话是若干**松散义群**，英语要把它们装进**一个以动词为核心的结构框架**：「向该厂订购三台车床」不是逐词摆放，是 `place an order for three lathes with the factory` 的槽位填充。步骤：**切义群 → 找结构核心（动词+名词+介词的固定框架）→ 按语义角色入槽 → 检查槽位 → 验证语义相容性**（deepen 带不了 reform，缺的中介是 commitment to）。16 个汉英结构转换模式与操作细则见 `reference/techniques.md`。

- 介词决定语义角色（avenge her mother ≠ avenge himself **on** the killers），**这类搭配必须查证不能推**。
- 四字格分流：描述性 → 一个精准英文词（一丝不苟 → precise）；叙述性 → 英语现成习语（意象全换）；找不到对应 → 释义，不自造比喻。
- 「使/让」句不要条件反射译 make sb...；「随着」不要条件反射译 With...。

### 阶段 2 — 减法诊断（核心）九步流水线

对照 `reference/chinglish-symptoms.md` 逐段过。顺序有讲究，**两条硬约束不可颠倒**：消名词化必须先于修平行与补连接词（名词化不除，平行调不平、连接词无处挂载）；调语序必须先于补连接词（语序不定，连接词的落位与选词无法定夺）。

1. **删冗余**：范畴词（……工作/问题/情况/局面）、套语前缀（努力/大力/切实）、冗余修饰语、四字对偶双词（加强和改进 → 只留一个或换一个更准的词）。套语走**三分法**：引导套语删；中心谓语（「政府要高度重视 X」）保语义换地道表达（give high priority to），不删也不照搬 attach great importance to；拿不准政论档从保留。词表见 `reference/wordlists.md`。
2. **消名词化** ★收益最高的一刀：抽象名词 → 动词/动名词/形容词；due to / lack of → because 从句（会自动逼出动词与主语）；名词串 ≥3 拆介词结构。
3. **修垂悬**：句首分词/动名词/不定式的隐含主语必须 = 主句主语。汉语无主句直译是垂悬的最大来源——「通过……」「为了……，必须……」「作为X，……」逐一补主语或改从句。白名单（generally speaking / according to 等）之外一律按垂悬处理；`based on` 不在白名单。
4. **修平行**：并列串同词类；相关连词（not only...but also）同形；标题同模板；比较结构两端同类。**刻意重复关键词，抵抗中文式近义换词冲动**——英语平行靠重复同一个词强化。
5. **调语序**：核心断言压句末（end-focus），时间/地点/条件/目的前置，not X but Y 否定在前。新闻导语例外。
6. **补/改连接词**：汉语没写连接词 ≠ 英译不需要。补词优先级：因果 > 转折 > 增补。`while` 只留给时间同时；「随着」的 With 必须显化为 When/Because/Thanks to；and 表不了转折与因果。
7. **修代词**：先行词必须明说、唯一、紧邻、数一致（中国译者错误几乎全在**数**）。宁可重复名词，不要歧义代词。补出汉语省略的主语**正是译者的职责**，但无从判断施动者时宁可主语含糊也不造假主语；连续无主句补出的**主体全篇统一**（不得 Governments → We 漂移）。
8. **读音质检**：朗读，查同词同音紧邻重复、意外头韵。
9. **连锁自检**（每步之后都做）：删掉的名词是否是后文代词的先行词？新引入的 this 是否与旧 this 撞车？主谓搭配是否仍成立？**单个病症的修复会生成新病症。**

### 阶段 3 — 双轨质检 + 忠实度红线

- **轨道一**：不看中文，纯查英文内部逻辑（缺连接词？不平行？句子讲不通？）。**英文逻辑讲不通几乎必是误译**，回查。
- **轨道二**：对照中文逐句核查漏译的逻辑关系、被误判为「冗余」的实义。**删任何「重复」之前必须回原文一次**——两半用词的语义场若有区别，是译文丢了义项，不是原文冗余（Pinkham 因不懂中文在这里栽过跟头，我们能读原文，这步不许省）。
- **红线**：① 权威讲话的冗余改写不删除；② 拿不准的对偶词**两个都留**（"meaning must have priority over elegance"—Sol Adler）；③ 补词说白必须有原文或上下文依据，"You should think hard before adding the explanatory words."
- **压缩率自查**：合格的去 Chinglish 改写通常比逐词直译短 20%–50%。若译文与逐词直译长度几乎相同，多半只动了词没动结构。

### 阶段 4 — 机械扫描 ★（落盘后必跑）

```bash
python3 ~/.agents/skills/zh-en-translation-polish/scripts/chinglish_scan.py "<名称> 翻译(汉英对照).md"
```

脚本扫英文行（跳过 `> ` 中文行），报告：全角标点残留、空壳框架（the fact that / the situation in which）、套语动词短语、抽象名词后缀密度 ≥3 的句子、可疑连接词（句首 With / based on / while）、陈套强调副词密度。**每条警告要么改掉，要么在心里能说出保留理由**（术语、政治定式、hedging、引文）——警告是候选不是判决，这正是你和机器的区别。目标：无一条未经判断的警告。

英文正文一律半角标点；只有 `> ` 中文原文行保留全角。聊天里直接给的小段对照（未落盘）同样手动套用扫描项自查。

### 阶段 5 — 输出汉英对照

按下方格式逐段配对；成篇则写文件；给用户附一句「文体档位判定 + 主要取舍说明」。

## 汉英对照输出格式

**按段落配对**：中文原段作为 blockquote，紧接英文译文。

```markdown
> 我们向该厂订购了三台车床，希望能在月底前交货。

We placed an order for three lathes with the factory, and we hope they can be delivered by the end of the month.
```

规则：
- 英文正文用半角标点；全角标点只出现在 `> ` 中文原文行内。
- 标题作英文 `##`/`###`，不加 blockquote；可选地把中文标题作为上一行 blockquote。
- 不该被派生脚本删掉、需保留进全英文版的东西（图片、表格、标题块）**不要** blockquote。
- 公式/代码用共享代码块，不按语言重复。
- 只清理提取噪声（删页眉页脚页码），**不要**从英文反推中文。

## 润色边界 ★（防止方法论被用过头）

Pinkham 本人的立场比她的规则宽容得多，这层丢了 skill 就成了无差别删词机：

- **可疑短语「四次里有一次真有意义」**：见到不是删，是判断。三问：这个上下文里它被证成了吗？为本段句意所必需吗？还是只因汉语里有就搬进来了？同一个 follow a policy of，「动摇的政策」必删（自相矛盾），「和平共处政策」必留（政策就是句意）。
- **修饰语五级处置刚性**：纯冗余型（new innovations）→ 唯一可无脑删；自明型 → 首现可留再现删；强调型 → 可能因**政治定式**必须保留；弱化型 → 可能是**有意自谦**（邓小平 "accomplished its tasks fairly well"）必须保留；陈词型 → 高层表态宁留勿删。
- **拿不准就两个都留**——尤其是会被外国读者逐字研读的正式文本，「冒着保留冗余的风险，好过冒丢失原意的风险」。
- **不要为地道牺牲准确**：换同义词避免重复时必须语义等值；elegant variation 牺牲准确性就是本末倒置。

详表（文体打折、边界红线、准确性质检清单）见 `reference/text-analysis-and-qa.md`。

## 示例

输入（中文，政论体，档位判定：公文/外宣，Pinkham 规则全开）：

```
要进一步加强农业基础设施建设，切实做好防汛抗旱工作，努力实现粮食稳产增产。
```

输出（汉英对照）：

> 要进一步加强农业基础设施建设，切实做好防汛抗旱工作，努力实现粮食稳产增产。

We should strengthen agricultural infrastructure, ensure effective flood control and drought relief, and keep grain output stable and growing.

（取舍：「建设」范畴词脱落；「努力实现」套语不译，动作直接做谓语；「防汛抗旱」用官方定译 flood control and drought relief；「切实做好」不走 do a good job 套语，力度落为 effective——仿 Pinkham 对 "a good job must be done in medical-care work" 的处理：保力度、删壳；三个动宾并列统一为动词平行结构。）

## 致谢与许可

本 skill 的代码、提示词与组织方式以 **MIT 许可**发布。

方法论与判例蒸馏、转述自 Joan Pinkham《中式英语之鉴》（外语教学与研究出版社，2000）与陆国强《汉译英常用表达式经典惯例》（上海外语教育出版社）。`reference/` 各表中的少量引文系评注与教学目的的简短摘引，著作权归原作者与出版社所有；本 skill 仅为方法工具，不能替代原著，建议系统学习者购买正版。
