# Changelog

## [1.1.1] - 2026-10-07

- 明确所有文体共同遵守的忠实性边界，保留尝试、情态、范围、逻辑、宣称与修辞，不设压缩率或零警告目标。
- 增加原文覆盖与译文依据的双向核对，以及长文分段检查、发言者和图注归属检查。
- 校正文体指导、结构模式和参考例句，补充五组语义质量案例及独立评估方法，重写面向新用户的中英文 README。
- 修订机械扫描的标点与候选提示，识别常见代码、链接和表格结构；增加 15 项回归测试。未进行模型翻译实测。

- Apply fidelity boundaries across registers, preserving attempts, modality, scope, logic, claims, and rhetoric without compression or zero-warning targets.
- Add bidirectional coverage and grounding checks, chunked review for long texts, and speaker/caption attribution checks.
- Refine register guidance, structural patterns, and examples; add five semantic quality cases with a separate evaluation protocol and rewrite both READMEs for new users.
- Improve advisory scanning of punctuation and common code, link, and table structures; add 15 regression tests. Model translation performance was not tested.

## [1.1.0] - 2026-09-12

- 明确中译英及对照中文原文润色英文的触发范围，排除英译中、原创英文写作和单词查询。
- 短文本直接聊天交付；用户指定的单语、双语和文件目标优先，减少重复确认。
- 按文体选择检查，保留学术限定、官方定译、逻辑与原文的双轨质检要求。
- 明确独立安装使用，文档输入依据宿主实际可用的读取能力处理，并说明提取缺口。
- 版本与标签归入标准 metadata，同步中英文说明。

- Clarify Chinese-to-English translation and source-grounded polishing scope.
- Honor requested delivery formats and use register-sensitive checks without mandatory diagnostic display for short passages.
- Clarify standalone installation and document handling through available host tools.
- Preserve source fidelity and dual-track QA; align standard metadata and bilingual documentation.

## [1.0.0] - 2026-07-21

首个公开版本。保留原标签、发布说明和源码历史。

Initial public release. The original tag, release notes, and source history are retained.

[1.1.1]: https://github.com/HoraceLuBFA/zh-en-translation-polish/releases/tag/v1.1.1
[1.1.0]: https://github.com/HoraceLuBFA/zh-en-translation-polish/releases/tag/v1.1.0
[1.0.0]: https://github.com/HoraceLuBFA/zh-en-translation-polish/releases/tag/v1.0.0
