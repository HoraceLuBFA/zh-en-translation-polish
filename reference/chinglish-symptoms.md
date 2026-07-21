# 中式英语病症诊断表（汉译英九步流水线细则）

基于 Joan Pinkham《中式英语之鉴》十三章，按流水线顺序重组。每条含：汉语触发条件（什么中文会诱发它）→ 诊断测试（怎么机械地发现）→ 修法 → 判断边界（何时不改）。

**目录**：一 冗余词（范畴词/套语/修饰语/对偶）· 二 重复 · 三 名词瘟疫 · 四 垂悬修饰语 · 五 平行结构 · 六 语序与焦点 · 七 逻辑连接词 · 八 代词与先行词 · 九 读音与连锁自检

---

## 一、冗余词（流水线第 1 步）

### 1.1 范畴名词

**汉语触发**：「……工作/问题/情况/事业/局面/方面/领域/现象/状态/过程/任务/做法/行为/因素/关系/环节/水平」挂在实义名词后。

**诊断**：`X of Y` 且 X 是空壳总类词、Y 已是完整概念 → 删 X。反向检验：删掉后句意有无损失？

| 中文 | ❌ | ✅ |
|---|---|---|
| 计划工作中的严重错误 | a serious mistake in the work of planning | a serious mistake in planning |
| 推进和平统一大业 | promoting the cause of peaceful reunification | promoting peaceful reunification |
| 反对浪费现象 | oppose the practice of extravagance | oppose extravagance |
| 加上价格不稳定这一因素 | coupled with the factor of price instability | coupled with price instability |

**边界**：范畴名词偶有实义——"in accordance with **the principle of** self-reliance" 保留；"adopt a policy of" 在赎买 vs 没收的对比语境里是实义。

### 1.2 冗余名词（语义已被别处包含）

「加快……的步伐」→ accelerate 已含 pace；「农业上获得丰收」→ harvest 已含；「……性的」→ 形容词已含 in nature；「一系列/各种」→ 复数 -s 已含；「实现……化」「加强……的建设」→ the realization of / the building of 全删。
**边界**：时间词不总冗余——"**at present** it is necessary" 可能正是要说「只是暂时」。

### 1.3 空壳架子结构

grep：`the situation in which / a situation where / this state of affairs / the key to ... lies in / lies in the fact that / the fact that / is a subject that / constitute a period in which`。
Strunk 对 "the fact that" 的裁定："It should be revised out of every sentence in which it occurs."（"situation" 是 "a particularly dangerous noun"。）
修法：把架子后面真正的主谓提上来当主句。`the key to X lies in Y` → `X is to Y`。

### 1.4 范畴动词 + 名词

**汉语触发**：进行/加以/作出/予以/给予/实现/实行/开展/从事/搞好/取得/起……作用/产生……影响。

**诊断**：`V + (a/the) + N + of/in/to/on/over`，V ∈ {make, have, give, provide, conduct, carry out, engage in, achieve, accomplish, realize, bring about, place, exercise, register, implement, adopt, take, perform}，且 N 有同根动词 → 名词还原为谓语动词。被动式变体（an improvement must be made in）同样算。

速查：make an investigation of = investigate · make efforts to = try · have an influence on = influence · give guidance to = guide · provide assistance to = assist · achieve success in = succeed in · accomplish the modernization of = modernize · bring about an improvement in = improve · place stress on = stress · exercise control over = control · register an increase = increase。

### 1.5 引导性套语动词短语

**汉语触发词表**：努力/大力/积极/尽力/千方百计（→ make great efforts to / try our best to / strive to）；注意/重视/高度重视（→ pay attention to / attach importance to）；搞好/做好……工作/抓好（→ do a good job in）；采取措施/步骤（→ take measures to）。

**判据**：如果他们真做了那件事，就必然已经「努力/重视/做好」了 → 删前缀，动作直接做谓语。

**边界（原书明确保留的反例）**："we must **attach great importance to** scientific research institutes"——「重视」就是全句中心思想，只可改写不可删；"a good job must be done in medical-care work"——重点确实是「做好」，留 good 删 job → "good medical care must be provided"。

**★保留时的出口（三分法，不是二选一）**：判定「重视/努力/切实」是引导套语还是中心谓语——
- 引导套语（后面的动作才是重点）→ **删**，动作做谓语；
- 中心谓语（重视本身是政策优先级信号，如「政府要高度重视 X」）→ **保语义、换地道表达**：give (high/top) priority to X / prioritize X / focus on X——既不删丢力度，也不照搬 cliché 直译 attach great importance to；
- 拿不准 → 政论档从保留，一般文本从删。

### 1.6 多余修饰语（五类，处置刚性递减）

1. **冗余型**（new innovations / valuable treasure / final completion）→ 唯一可不犹豫直接删。
2. **自明型**（适当地/切实/充分/「国民」经济）→ 多数删；首现且确指「追加」可留（further），**同一词必要性随出现次数递减**。
3. **强调型**：强词被垫（serious chaos / firmly banned / broad masses）→ 删修饰语；弱词被垫（extremely important）→ 合并成一个强词（essential / imperative）；四大默认删：active(ly)、effective(ly)、actual(ly)、successful(ly)。**但可能因政治定式必须保留**（"the complete prohibition and thorough destruction of nuclear weapons"）。
4. **弱化型**（比较/基本上/或许 → quite, rather, fairly, basically, perhaps）：无逻辑理由则删，perhaps/maybe → may/might。**但有意自谦必须保留**（"accomplished its tasks fairly well"—邓小平；学术 hedging 全部保留）。
5. **陈词型**（resolutely, unswervingly, vigorously, conscientiously）：密度指标**每页 ≤2 次**；删或换新词（arduous → demanding）。高层公开表态宁留勿删。

**四问决策树**：必要吗？该带进英文吗？该连同被修饰词换一个更强的词吗？还是删？
名家判据：选强词就要信任它独立站住（"I reject the accusation" 强于 "I utterly reject"）；用形容词标示**种类**而非程度（an economic crisis ✓，an acute crisis ✗）。

### 1.7 冗余对偶（redundant twins）

**汉语触发**：四字并列偏好——讨论研究/挫折失败/经验教训/困难和问题/权利和利益/支持和帮助/巩固和发展/加强和改进/审议并通过/培育和发展/情况和特点/体制和结构。

**关键提问**：不是「这两个词有区别吗」（任何两个英文词都有区别），而是 **"In this context, does the second word add anything significant?"**

**三条修法按序**：① 删其一（留更具体者）；② 两者皆换成一个更准的词（faraway, distant areas → remote；importance and urgency → priority）；③ 补词澄清（conditions and environment → working conditions and social environment）——补词是把汉语隐含的意思明说，**有误译风险，动手前想清楚**。

**★缺省规则（反直觉）**：拿不准就**两个都留**。"It is generally better to risk including a redundancy than to risk losing an element of the intended sense."（Sol Adler："meaning must have priority over elegance."）文体定尺度：党代会讲话全保留，报纸社论毫不犹豫删。
原书判定必须两个都留的例：意见和要求 opinions and demands / 权利和利益 rights and interests / 稳定与安全 stability and security / 审议并通过 examined and adopted。
**反模式**：英语母语者也写 "strengthen and enhance"——不能因为「英语里也有」就放行。豁免仅限法律术语（null and void, each and every）与头韵诙谐语。

---

## 二、重复（第 1 步续）

**总原则**（Follett）：同一篇文字里，同一个意思不应作为新信息出现第二次。

### 2.1 三类重复及汉语病灶

| 类型 | 英文模式 | 汉语病灶 |
|---|---|---|
| 简单复述 | arrive on time **and** be punctual | 四字对偶骈句（厉行节约、减少开支）；译者给意合句自补 and 造出 A→A 循环 |
| 不言自明 | arrive on time **in order to catch the train** | 「以/以便/从而」引出的**定义性目的**（设立防疫机构以预防兽病） |
| 正反镜像 | arrive on time **and not be late** | 「不是……而是」「决不……而要」「要……不要」 |

### 2.2 处理顺序 ★

1. **先回查中文求异义**（首选，原书称「此类改动最为成功」）：英文两半看似同义 → 回原文，语义场有区别就是译文丢了义项（「交通」= transportation 还是 communication？「专业革命家」还是「革命的专业人员」？）。**英文逻辑讲不通（"strategy serves the past"）几乎必是误译。**
2. 确认无新义才删（删较空泛的那半；三重表述至少砍到两重）。
3. 无权删则弱化（法律/正式声明）：换措辞（unity → solidarity）、上位词、换句法位置——是妥协不是首选。

**允许保留**：对立两半指向不同主体/时段（我们必胜，敌人必败）；价值宣示（这是好事，不是坏事）；作者标志性文风（毛著英译）。保留必须是例外。

### 2.3 重复指称：先判「该不该指」，再判「用多长的形式指」

**必须保留**的三判据：删后本句失去主语/所指（连贯性）；该实体承载本句新论断（定义句里的 socialism）；直接引语与条约原文**不得改写不得缩略不得代词化**。

**六种缩短手法**：do so/do this（先行动作必须唯一且主动语态）· 删修饰语留中心词（the Conference）· 指示/物主词（that principle / such ventures / their development）· 概括名词（these matters / the two / this document）· 代词（词频判据：同一实词一句 ≥3 次或四句 ≥5 次须削减）· 首字母缩略（≥3 词专名出现 ≥3 次；首现全称+括号缩略）。

**清晰度优先于简洁**：宁用 their development 不用 it；former/latter 仅限上文明确两项。即使改后字数没少，消除紧邻重复仍是改进；但换同义词必须语义等值。

---

## 三、名词瘟疫（流水线第 2 步 ★收益最高）

**汉语触发**：「……的实现/提高/加强/调整」（「的」字把任何动词挂成名词）；「……化」；「缺乏/由于/为了」（介词框架必然引出名词）；「进行/加以 + 双音节动词」。

**机械诊断**：
1. 一句里 `-tion/-sion/-ment/-ance/-ence/-ity/-ness/-ship/-al/-ure/-age/-cy` 结尾名词 ≥2 报警、≥3 必改。
2. 对每个抽象名词问「**谁**做的？做的**什么**？」答不出 → 改。
3. 主要动词是 is/constitutes/lies in/serves as/results from 这类空转系动词 → 真动词被名词吃掉了。

**对治四法按序试**：

| 法 | 适用 | 例 |
|---|---|---|
| ① 换动词（最优先） | 有同根动词 | Analysis is necessary even for the imperialist camp → It is necessary **to analyze** even the imperialist camp |
| ② 换动名词 | 名词占主语/介词宾语位 | economic revitalization will be arduous → **revitalizing the economy** will be arduous；through cooperation with → **by cooperating with** |
| ③ 换形容词/副词 | 表性质（-ness/-ity） | prove the correctness of these policies → prove that these policies **are correct**；blindness in action → acting **blindly** |
| ④ 说白（备用，风险最高） | 仍答不出谁对谁做什么 | give full scope to the role of experts → take full advantage of the knowledge and abilities of experts |

②是中途站不是终点；④补词必须对解读负责，上下文不足时**宁可保留含糊，不写错误解释**。

**★修复不得收窄语义**：名词化修复会把开放概念变具体判断——「探索模型压缩的可能性」改成 explore whether the model can be compressed 就把开放的技术探索（剪枝/量化/蒸馏皆可）收窄成二元判断；此时用 investigate model compression techniques 之类保留覆盖面的动词结构。每次消名词化后回问一句：语义外延变小了吗？

**关键杠杆**：due to / as a result of / lack of → **because 从句**，会自动逼出动词与主语：
- This resulted from our lack of vigilance → This was partly **because we were not sufficiently vigilant**
- auctioned off as a result of its loss-making operation → auctioned off **because it was operating at a loss**

### 3.1 名词串（名词当形容词）

**根因**：汉语字与字之间不写连接成分，机构名/项目名天然是名词串，直译即灾（`China Foreign Experts Employment Contract Disputes Arbitration Commission`）。

**分级**：1 个名词作定语合法（income tax）；2 个须一望可知（water conservancy project）；**≥3 一般规则不允许**，例外仅限大写绑定的专名。

**四法**：转词类（soil erosion control → to control soil erosion）→ **加介词**（economic recovery period → the period **of** economic recovery；一般优于连字符）→ 加连字符（固化复合形容词）→ 说白。
**防误报**：判据是**读者熟悉度不是长度**——同一句里 geographical constituency demarcation 被拆，voter registration 保留。学科内已成术语的不拆（attention mechanism, machine translation）。

---

## 四、垂悬修饰语（流水线第 3 步）

**核心规则**：句首分词/动名词/不定式短语的隐含主语必须 = 主句主语；作形容词用的介词短语黏附主语。复合句里参照**所属小句**的主语。

**汉语无主句直译是垂悬的最大来源**——五类映射：

| 汉语结构 | 产生 | 首选处置 |
|---|---|---|
| 「经过/通过/在……中/这样做」+ 无主句 | 垂悬动名词（最高发） | 补 we/you 作主句主语，或改带主语的从句 |
| 「为了……，必须（努力/采取措施）」 | 垂悬不定式 | `we must + 动词`，顺带消灭 efforts/measures 假主语 |
| 受事主语句 /「……，使/从而……」 | 垂悬分词 | 改主动补施事；或 -ing → which 从句 / 同位语（an increase of 23%） |
| 「作为X，……」话题≠主语 | 垂悬介词短语 | 补主语（As leaders, **we** must...）或改 Since I am... |
| 与主旨无关的人物描写定语 | 垂悬形容词 | **直接删**（本章唯一推荐删的一类） |

例：「通过裁员，公司的年度负债下降了」→ ❌ by cutting employees, **the annual debt** has decreased → ✅ by cutting employees, **the firm** has reduced its annual debt。
「凭借优越环境，任何投资都能获得回报」→ ❌ With a favorable environment, any **investment** is assured → ✅ **Because Jiangxi Province has** a favorable environment, any investment there is assured of healthy returns。

**白名单（防误报）**：generally speaking / judging from / barring / owing to / according to / provided (that) / concerning / regarding / assuming / allowing for / granted that。`considering` 作介词安全、带副词修饰时仍是分词。**`based on` 不在白名单**（→ On the basis of / In light of / Having studied）；`in order to serve you better` 类不豁免。裁定立场保守：**白名单外一律按垂悬处理。**

---

## 五、平行结构（流水线第 4 步）

**根本差异**：中文并列靠语义同类成立，英语靠**语法同类 + 语义同类**双重成立。动笔前先为每串定统一词类（阶段 0.B 已做，这里核验）。

四个强制区：

1. **并列连词**（and/or/but/nor）：写出每项的类型，三项以上须**全部**同类。修法：少数派改成多数派；统一后仍别扭 → 它们逻辑上本不可比，弃用并列。灰区：名词与动名词混用无歧义可放行。
2. **相关连词**（both...and / not only...but also / either...or）：比①更严，要求**逐字对齐**——介词对介词、从句对从句。`on the one hand/on the other hand` 按相关连词处理；`no sooner...than` 零自由度。
3. **列表与标题**：`First... Second... Third` 各项同句型模板。**汉语公文动宾排比标题是高频灾区**——先扫完全部同级标题再定模板，首选 gerund（能吸收无主语动宾而不必编造主语），跨页也不豁免。
4. **比较结构**（like / than / as...as）：两端必须同类事物——「与皇冠假日酒店一样，所有客房均配备……」→ Like **the rooms in** the Crowne Plaza, all **those in** the Holiday Inn feature...；tax receipts greater than **last year** → than **they were last year**。

**精细化五项**：并列名词同为抽象或同为具体；动词语态统一；短语内部结构统一（allocation of land, **reduction of** rents, **increase in** wages）；**刻意重复关键词与句型模板**（中英审美正面冲突：中文近义换词避重复，英语平行靠重复强化——from their point of view... from the overall point of view）；同类状语占同一位置。

**误导性平行**：形式平行但逻辑不平行——各项回答的不是同一个问题（品质 vs 尺寸）、一项是另一项的后果（行军与疲劳 → the exhaustion of constant marching）、存在层次混杂（deaths / the wounded / deserters → 统一为三个事件或三类人）。兜底判据：**起不出共同的上位名词就是不同类。**

---

## 六、语序与焦点（流水线第 5 步）

### 6.1 就近咬合（逻辑线）

每个介词短语/分词短语/关系从句，与**紧邻左侧的名词或动词**组成最小短语念一遍——事实上讲不通（钱不能治病、干部不选干部）→ 位置错。**跨过 that 的状语一律重查**（修饰主句动词还是从句动词：After years of effort, Gao said that... 变成「高经过多年努力才说」）。
边界：就近读法讲得通就不算错；「读者能猜对」不构成免责。

### 6.2 尾重与句末焦点 ★汉英最系统性的冲突

英语句末是最强焦点位（Strunk & White）。汉语前重心 + 尾巴甩状语，直译必然让次要成分夺权。

**诊断**：① 遮住整句只读最后 5–8 个词——这是本句最想让读者记住的吗？② 句末是纯时间/地点/来源/「以促进……」→ 几乎必错。③ 下一句展开的概念不是本句句末概念 → 焦点放错了人。

**三位法**：句末 = 核心断言；句首 = 次要框架（日期、衔接）；句中 = 细节、原因、来源（长块沉中间不会被淹没）。
配套：why 在 what 前（To promote the exchange of commodities, **we should set up**...）；negative 在 positive 前（not in light of our habits but **from the point of view of 600 million people**）；从属句前置主句压末。

例：❌ they reached the Dabie Mountains **in late August** → ✅ **In late August,** after twenty days of exhausting marches, **they reached the Dabie Mountains**.

**边界**：新闻导语例外（消息来源置句末是行业惯例）；焦点取决于上下文不是单句；几个次要短语内部次序自由；**改完读着别扭多半是焦点判断本身错了**。

### 6.3 主从裁决

汉语小句平铺无连词、权重相等——所有小句都译成 and 并列句 = **未做裁决**。判定主句（承载核心断言者），其余改 although/when/if/since 从句前置。多条件 → 一串平行 if 从句在前，结论压末。

---

## 七、逻辑连接词（流水线第 6 步）

**铁律**：汉语原文没有连接词 ≠ 英译不需要。"When relations between ideas have only to be **suggested** in Chinese, they must be **plainly stated** in English." 不加连接词的译文是 "a plate of loose sand"。

**补词决策流程**（对每对相邻分句 S1, S2）：
1. 判关系（读完 S1 写下「读者预期 S2 说什么」；不符 → 转折/让步；是后果 → 因果；加强 → 递进）
2. 现有词汇已显性表达？→ 查是否用错（见 7.2）
3. 自明到无需标记？（遮住 S2 首短语读者能预判方向 → 可不加）
4. 加词位置：转折词优先句中逗号夹住（In March 1983, **however**, ...），需强调才句首
5. 重读整段，别连续三句都挂连接词

**优先级：因果 > 转折 > 增补**（因果缺失丢核心意义；转折缺失误导；增补缺失只是读起来跳）。实践偏向**补**——中国译者的风险从来是补得不够，不是补得太多。十二类连接词查词表见 `wordlists.md`。

### 7.1 可疑连接词：while 与 with

**while 替换测试**：分别代入 during-the-time-that / although / whereas / and——**多于一种读得通 = 歧义，必改**；只有 and 读得通 = 滥用。默认策略：**while 只留给时间同时**；对比用 whereas / on the other hand（注意 while/whereas 从句**不能独立成句**，断句只能用 On the other hand）；让步用 although。

**with 是汉译英特有灾区**（「随着……」条件反射译 With）。合法五类：伴随/施事/特征/方式/所属。之外问它真想表达什么：

| ❌ 万能 with | ✅ |
|---|---|
| **With** the rapid increase of production..., Chen was promoted | **When** production began to increase rapidly... |
| **With** professionals familiar with the law, these offices... | **Staffed by** professionals... |
| It was **with** her leadership that... | It was **thanks to** her leadership that... |
| **With** China's vast territory, ... | **Considering** China's vast territory... |
| **With** wide streets and a small population, the city is filled with... | The city **has** wide streets... **It is** filled with...（无逻辑关系就拆句，不硬缝） |

### 7.2 用错的连接词

**根因：汉语「和/而/也」的语义宽度远大于英语 and。**

- 「公有制为主体，**也**有其他成分」→ and 错，**but** there are also others（「也」实为转折）
- 「新建**和**改建公路」→ build **or** upgrade（同一条路不能既建又改；未存在的路不能加 the）
- 「中国缺资金，有很多资源未开发」→ 中文是因果：short of funds **and for that reason** unable to develop...
- 「正因为难，更应重视」→ Difficult as it is = although，反了 → **Precisely because** it is so difficult
- 「再过六年，到1960年」→ six years **later** 参照上文年份（会被算成 1962）；说话时刻参照用 six years **from now**

专项测试：and → 两项能否同时成立？不能改 or。also/besides/likewise → S2 是支持还是削弱 S1？削弱换转折词。有时正确操作是**删**（Besides 把核心论据降级）；有时须同时改内容（补 particularly 才构成真对比）。类别对了即可，选词有自由度。

---

## 八、代词与先行词（流水线第 7 步）

**四条总则**：先行词必须 ① 明说 ② 无歧义 ③ 紧邻 ④ 数一致。**兜底修法：扔掉代词写名词——宁可重复，不要歧义。**

1. **未明说**：汉语省主语，译者随手补 it/this/they。补出隐含主语**正是译者的职责**（"it is precisely the translator's duty to identify those ideas that a native speaker of Chinese understands by implication"），不能丢个 it 蒙混；但无从判断施动者时宁可主语含糊（lack → **no** sense of urgency）也不造假主语。`do so/do that` 的先行动作必须是**主动语态**。**补出的主体全篇一致**：汉语「要……。要……。」连续无主句默认同一施政主体，英译不得一句补 Governments at all levels 下一句漂移成 We——先定全篇主体（或统一非人格化表达），再逐句补。
2. **歧义**：≥2 个数性匹配的候选。注意**句子主语对代词有超强吸引力**。修法要领：把第一个歧义代词换成名词，其后代词自动统一归位。
3. **太远**：中间夹任何一个数性匹配的名词就算远。**关系代词必须紧贴先行词**——which 指整个前句时，把概念概括成名词塞到 which 前（..., **an operation in which** he played a key role / **a struggle which**...），或拆句（**This statement** is...）。这类错常是硬错不是歧义（"to shatter the Gang of Four, in which he played an important role"）。
4. **不一致**：**中国译者错误几乎全在数**（汉语无单复数形态）。every/each/anyone/someone 一律单数；修法二选一：改代词就先行词，或**改先行词就代词**——单数导致别扭或被迫写 he or she 时，把先行词改复数（Every top official → **All top officials**... they），更顺且回避性别问题。

**灰色地带（防过度修改）**：集体名词（media/government/committee）单复任选一派**但全文一致**；singular they 正式译文回避（改复数先行词最省事）但**人称漂移（their→your）任何语体都是硬错**；被中间复数名词带偏、修饰语错位荒谬（cow that does not smoke or drink）是硬错必改。

---

## 九、读音与连锁自检（流水线第 8–9 步）

**读音**：朗读。同一个词/同一个音在一句一段内反复撞击（Some-suffered-serious-setbacks 的 s 串）→ 换同义词（语义等值前提下）、换指代、重构句法。「生厌的临界点来得非常快。」

**连锁自检（每一步删改之后都做，不是最后做一次）**：
- 每个 it/them/this/their 是否仍有唯一先行词？（刚删掉的名词可能正是先行词）
- 是否新造出紧邻重复？（新引入的 this 与前文 in this way 撞车 → 把前文改成 Only then）
- 主谓搭配是否仍成立？（删掉 situation 后 thriving 的主语是谁 → literature and art **flourish**）

原书示范：单个病症的修复会生成新病症（去垂悬 → which 挂错 → 归位 → 状语离动词太远 → 三次迭代才收尾）。**流水线每步之后重跑诊断，而非一次通过。**
