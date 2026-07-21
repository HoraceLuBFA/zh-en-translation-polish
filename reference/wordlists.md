# 词表（汉语触发词 + 英语警戒词）

供人工排查与 `scripts/chinglish_scan.py` 机械扫描共用。所有命中都是**候选不是判决**——每条要么改，要么能说出保留理由（术语/政治定式/hedging/引文）。

## 一、汉语侧触发词（读原文时警觉）

| 类 | 词表 | 诱发 |
|---|---|---|
| 范畴词 | 工作 问题 情况 事业 局面 方面 领域 现象 状态 过程 任务 目标 做法 行为 因素 关系 环节 水平 事情 境地 | 空壳名词（the work of / the situation of） |
| 范畴动词 | 进行 加以 作出 予以 给予 实现 实行 实施 开展 展开 从事 搞好 做好 取得 获得 起…作用 产生…影响 | 虚动词+名词（conduct/carry out/make + N） |
| 套语前缀 | 努力 大力 积极 尽力 竭尽全力 千方百计 着力 · 注意 重视 高度重视 着重 切实 · 搞好 抓好 办好 · 采取措施 采取步骤 | make great efforts to / attach importance to / do a good job in / take measures to |
| 强调词 | 大力 有效 切实 真正 确实 一定 必将 坚决 彻底 全面 充分 深入 广泛 极大 高度 严重 巨大 伟大 广大 一小撮 成功地 胜利地 | 冗余 intensifier |
| 弱化词 | 比较 相当 较为 基本上 大体上 有些 稍微 或许 也许 可能 一定程度上 | quite / rather / basically / perhaps（学术档＝hedging 保留） |
| 对偶对 | 讨论研究 挫折失败 经验教训 困难和问题 权利和利益 意见和要求 支持和帮助 巩固和发展 改革和完善 加强和改进 培育和发展 审议并通过 制定和实施 情况和特点 体制和结构 影响和作用 | redundant twins |
| 名词化 | …的实现 …的提高 …的加强 …的调整 …的完成 …的发展 …化 缺乏… 由于… 为了… | noun plague |
| 无主句框 | 经过… 通过… 在…中 这样做 为了…必须… 作为X，… 随着… | 垂悬修饰语 / 万能 with |
| 万能连词 | 和 而 也 同时 并 | and 误覆盖转折/因果/选择 |

## 二、英语侧警戒词（扫描译文）

### 2.1 空壳框架（见到先试删/重构）

`the fact that` · `the situation in which` · `a situation where` · `this state of affairs` · `lies in the fact that` · `the key to ... lies in` · `is a subject that` · `constitute a period in which` · `in the field of` · `in the sphere of` · `the work of` · `the cause of`(政治义) · `the practice of` · `the phenomenon of/that` · `the process of`(泛指)

### 2.2 空壳/范畴名词（无实际信息即删）

situation, condition(泛指), problem(泛指), question(泛指), work, task, job, activity/activities, matter, issue(泛指), process, practice, phenomenon, cause, factor, aspect, respect, field, sphere, area(抽象), sector, level(抽象), degree, scale, extent, scope, role, function, character, nature, status, state, sense, spirit, atmosphere, measure(泛指), method(泛指), way(泛指), form, style, system(泛指), objective, goal, purpose, requirement, basis, foundation, means, efforts, attention, importance, significance

### 2.3 套语动词短语（默认删，动作直接做谓语）

make (great/every) efforts to · exert efforts to · try our best to · do our utmost to · pay attention to · pay heed to · attach importance to · lay stress on · do a good job in/of · make a success of · take measures to · take steps to · adopt a policy of(判断三档) · make an improvement in · conduct a/an ... of · carry out the ... of · give guidance to · provide assistance to · exercise control over · register an increase · place stress on · achieve success in · bring about an improvement · give play to · give full scope to · play a role in · is of great significance

### 2.4 抽象名词后缀（密度扫描：一句 ≥2 报警 ≥3 必改）

`-tion -sion -ment -ance -ence -ity -ness -ship -ism -al -ure -age -ancy -cy -hood -sis`

### 2.5 「必然引出名词」的介词框架（→ 换连词/动词）

due to · owing to · as a result of · resulted from · in view of · with regard to · in the course of · for the purpose of · in the process of · by means of · on the basis of · through the ... of · lack of · shortage of · absence of · in terms of
→ 首选替换：because / when / if / by V-ing / to V

### 2.6 陈套强调副词（每页 ≤2 次）

resolutely, unswervingly, vigorously, conscientiously, energetically, persistently, unremittingly, diligently · 四大默认删：actively, effectively, actually/truly/really, successfully · 其他：firmly(垫强词时), thoroughly, totally, completely(垫强词时), broad masses

### 2.7 可疑连接词

- 句首 `With ...,`（「随着」条件反射）→ When / Because / Thanks to / Staffed by / Considering / for all，或拆句
- `while`（非时间义）→ although / whereas / on the other hand
- `based on` 句首 → On the basis of / In light of / Having studied
- `in order to` → 多可删 in order
- `and` 连接逻辑上不能同时成立的两项 → or
- `and so / therefore` 滥用 → 核实因果是否真成立

### 2.8 垂悬白名单（防误报，不改）

generally speaking · judging from/by · barring · owing to · according to · provided (that) · concerning · regarding · assuming · allowing for · granted that · considering(介词义)
**不在白名单**：based on · in order to serve you better 类

## 三、十二类逻辑连接词查词表（按关系补词）

| 关系 | 候选词 |
|---|---|
| 因果 ★缺失最伤 | because, since, so, thus, therefore, accordingly, as a result, consequently, for this reason, thanks to |
| 转折 ★次伤 | but, however, yet, nevertheless, on the contrary, instead, on the other hand, whereas |
| 增补 | and, also, moreover, besides, furthermore, what is more, indeed |
| 让步 | although, though, granted, to be sure, of course, admittedly, it is true that |
| 条件 | if, unless, otherwise, provided that, once |
| 目的 | to, in order that, so as to, to this end, with a view to |
| 时间 | after, then, meanwhile, while, when, until |
| 逻辑顺序 | first, second, next, finally, in the first place |
| 举例 | for instance, for example, namely, such as, specifically |
| 强化 | indeed, in fact, what is more, let alone, precisely because |
| 复述 | that is, in other words, namely |
| 结论 | thus, so, in short, to sum up, all in all |

## 四、范畴动词配对速查（虚动词短语 → 单动词）

make an investigation of=investigate · make a careful study of=study carefully · make a decision to=decide to · make a proposal that=propose that · make an analysis of=analyze · have a dislike for=dislike · have trust in=trust · have an influence on=influence · have respect for=respect · have the need for=need · give guidance to=guide · provide assistance to=assist · carry out the struggle against=struggle against · conduct reform of=reform · engage in free discussion of=discuss freely · achieve success in=succeed in · accomplish the modernization of=modernize · realize the transformation of=transform · bring about an improvement in=improve · place stress on=stress · exercise control over=control · register an increase=increase
