# AI 资料调研助手 Agent

用 Python 从零构建可自定义的资料调研助手：接收研究问题，搜索资料、阅读网页、核对来源，并生成带引用的中文报告。

## 当前状态

项目初始化已完成，包含 Python 包结构、命令行入口和开发路线。

**搜索、网页阅读、模型调用、来源核对和报告生成尚未实现。** 当前命令行仅提供帮助与版本信息，不会访问网络或调用模型 API。

## 开发目标

先实现一个单 Agent，由项目代码控制工具调用循环、任务状态、停止条件和执行记录。

```text
研究问题 → 模型选择下一步 → 执行工具 → 记录结果
                  ↑                        │
                  └──── 需要补充资料 ──────┘
                                           │
                                    资料充分或达到上限
                                           ↓
                                   输出带来源的报告
```

计划中的首批工具：

- `search_web`：检索候选来源，返回标题、链接和摘要。
- `read_page`：读取网页正文与可获得的发布日期。
- `save_report`：将中文报告及引用保存到本地。

模型供应商、搜索服务和引用数据结构将在功能开发时确定。

## 本地开发

要求 Python 3.11 或更高版本。

```bash
cd ~/Desktop/ai-research-agent
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
ai-research-agent --help
ai-research-agent --version
```

也可以通过模块入口运行：

```bash
python -m ai_research_agent --help
```

`.env.example` 暂时只记录计划中的配置项；当前代码不读取 `.env`。

## 项目结构

```text
ai-research-agent/
├── README.md
├── pyproject.toml
├── .env.example
├── .gitignore
├── src/
│   └── ai_research_agent/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       └── tools/
│           └── __init__.py
├── tests/                      # 后续功能测试
└── reports/                    # 本地报告，默认不提交 Git
```

## 开发路线

1. 实现最小模型调用与自定义工具调用循环。
2. 接入搜索、网页读取，保存来源信息与工具执行记录。
3. 实现资料补查、中文报告生成与引用核对。
4. 加入最大步数、超时、错误恢复和成本记录。
5. 用真实研究问题评估来源质量、引用准确性和任务完成情况。

示例验收任务：查找 Karpathy 关于全球 AI 使用分层的原始发言，核对日期和人数，并区分个人估算与正式统计。

## 开发约定

- 初期以理解和实现工具循环为主，依需求逐步引入框架。
- 区分原始来源、转述和推断；资料不足时明确说明。
- 工具失败必须保留真实错误，不生成伪造的搜索结果或引用。
- 密钥、本地配置、运行日志和调研报告不提交到 Git。

## 仓库

[LazyDreamingDog/ai-research-agent](https://github.com/LazyDreamingDog/ai-research-agent)
