# GEO (Generative Engine Optimization) System

## 概述

GEO 系统是 Claude Code SEO Assistant 的核心功能模块，专门针对 AI 搜索引擎（ChatGPT、Claude、Perplexity、Google SGE）进行优化，提升内容在生成式搜索结果中的可见性和引用率。

## 系统架构

### 核心组件

```
geo-system/
├── skills/geo-optimizer/          # GEO 优化技能
│   ├── skill.md                    # 核心技能定义
│   ├── templates/                  # 内容模板
│   │   ├── ai-citation-optimization.md
│   │   ├── llm-content-structure.md
│   │   └── entity-relationships.md
│   └── resources/                  # 参考资源
│       ├── ai-search-engines.md
│       └── citation-patterns.md
├── commands/                       # GEO 命令
│   ├── geo-content-audit.md
│   ├── geo-entity-extraction.md
│   ├── geo-citation-monitor.md
│   ├── geo-competitor-compare.md
│   └── geo-visibility-report.md
├── docs/                           # 文档
│   ├── geo-optimization.md
│   └── geo-best-practices.md
└── .claude-flow/cache/             # 数据存储
    ├── config/
    │   └── geo-config.json
    ├── templates/
    ├── history/geo/
    └── reports/geo/
```

## 核心功能

### 1. GEO 内容审计 (`geo-content-audit`)

**功能：** 分析内容在 AI 搜索引擎中的引用优化潜力

**使用示例：**
```bash
/geo-content-audit your-article.md
/geo-content-audit https://yoursite.com/article --detailed
/geo-content-audit post.md --engines chatgpt,claude --output json
```

**输出：**
- 6 维度评分（权威性、实体关系、内容结构、数据质量、引用密度、技术优化）
- 引用障碍分析（按优先级排序）
- 具体优化建议（包含代码示例）
- 预期改进效果

### 2. 实体提取 (`geo-entity-extraction`)

**功能：** 从内容中提取实体并构建知识图谱

**使用示例：**
```bash
/geo-entity-extraction blog/post.md
/geo-entity-extraction post.md --format Article
/geo-entity-extraction https://yoursite.com --format FAQPage
```

**输出：**
- 识别的核心实体（人物、组织、概念、地点、事件）
- 实体关系分析
- Mermaid 知识图谱
- Schema.org JSON-LD 标记

### 3. 引用监控 (`geo-citation-monitor`)

**功能：** 监控 URL 在 AI 搜索引擎中的引用表现

**使用示例：**
```bash
/geo-citation-monitor --url "https://yoursite.com" --period 30
/geo-citation-monitor --url "https://yoursite.com" --engines chatgpt,claude
/geo-citation-monitor --url "https://yoursite.com" --compare "comp1.com,comp2.com"
```

**输出：**
- AI 引用次数和趋势
- 可见性评分变化
- 引用上下文分析（情感、位置、完整性）
- 竞争对手对比

### 4. 竞争对比 (`geo-competitor-compare`)

**功能：** 对比多个网站的 AI 搜索表现

**使用示例：**
```bash
/geo-competitor-compare --you "yoursite.com" --competitors "comp1.com,comp2.com"
/geo-competitor-compare --you "yoursite.com" --competitors "comp1.com" --deep-analysis
```

**输出：**
- 综合对比表格
- 优劣势分析
- 快速获胜机会
- 超越策略和路线图

### 5. 可见性报告 (`geo-visibility-report`)

**功能：** 生成 AI 搜索可见性综合报告

**使用示例：**
```bash
/geo-visibility-report --domain "yoursite.com" --period 30
/geo-visibility-report --domain "yoursite.com" --period 90 --format html
/geo-visibility-report --domain "yoursite.com" --format json
```

**输出：**
- 执行摘要
- 详细分析（各引擎表现）
- 内容优化建议
- 竞争对手对比
- 行动计划和预期成果

## 评分系统

### 6 维度评分（总分 100）

| 维度 | 权重 | 评分标准 |
|------|------|---------|
| **权威性** | 20 分 | 作者信息（7）、引用来源（7）、时间戳（6） |
| **实体关系** | 20 分 | 概念定义（7）、Schema标记（7）、内部链接（6） |
| **内容结构** | 20 分 | 段落长度（7）、标题层级（7）、概念密度（6） |
| **数据质量** | 20 分 | 准确性（7）、新鲜度（7）、完整性（6） |
| **引用密度** | 10 分 | 关键词密度（5）、语义相关（5） |
| **技术优化** | 10 分 | 结构化数据（5）、性能优化（5） |

**评分等级：**
- **85-100 分：** 优秀（AI 引用率 >70%）
- **70-84 分：** 良好（AI 引用率 50-70%）
- **55-69 分：** 一般（AI 引用率 30-50%）
- **<55 分：** 需要优化（AI 引用率 <30%）

## AI 搜索引擎特性

### ChatGPT (OpenAI GPT-4)
- **偏好：** 权威性、结构清晰、数据详实、实用性强
- **优化重点：** 作者资质、层级结构、最新数据、工具推荐
- **引用率：** 目标 65%+

### Claude (Anthropic)
- **偏好：** 实体关系清晰、逻辑严密、深度分析、多角度视角
- **优化重点：** 概念定义、论证结构、深度分析、平衡观点
- **引用率：** 目标 60%+

### Perplexity AI
- **偏好：** 信息准确、来源可靠、内容全面、时效性强
- **优化重点：** 事实核实、引用来源、全面覆盖、定期更新
- **引用率：** 目标 70%+

### Google SGE
- **偏好：** E-E-A-T 信号强、结构化数据完整、内容更新频繁
- **优化重点：** E-E-A-T、Schema.org、内容新鲜度、用户体验
- **引用率：** 目标 55%+

## 快速开始

### 1. 审计现有内容

```bash
/geo-content-audit your-article.md
```

### 2. 优化内容

根据审计报告的优化建议，优先处理高优先级问题：
- 添加作者 Schema.org 标记
- 优化核心概念定义
- 改进内容结构
- 更新数据和统计

### 3. 监控效果

```bash
/geo-citation-monitor --url "https://yoursite.com" --period 30
```

### 4. 对比竞争对手

```bash
/geo-competitor-compare --you "yoursite.com" --competitors "comp1.com,comp2.com"
```

### 5. 生成报告

```bash
/geo-visibility-report --domain "yoursite.com" --period 30
```

## 最佳实践

### 内容创作

1. **使用 LLM 友好的结构**
   - 在前 100 词给出清晰定义
   - 段落长度 50-150 词/字
   - H1-H6 层级清晰
   - 添加 TL;DR 和 FAQ

2. **建立权威性**
   - 添加完整的作者 Schema.org 标记
   - 引用 5-10 个权威来源
   - 包含案例研究和数据
   - 定期更新内容

3. **优化实体关系**
   - 核心概念有明确定义
   - 构建知识图谱
   - 使用 Schema.org 标记
   - 建立内部链接网络

### 持续优化

**每周：**
- 监控 AI 引用变化
- 分析引用模式
- 更新关键数据

**每月：**
- 审计 GEO 表现
- 对比竞争对手
- 优化薄弱环节

**每季度：**
- 全面策略审查
- 更新 Schema.org 标记
- 调整优化方向

## 配置文件

### GEO 配置 (`geo-config.json`)

```json
{
  "version": "1.0.0",
  "aiEngines": {
    "chatgpt": { "enabled": true, "priority": "high", "weight": 1.0 },
    "claude": { "enabled": true, "priority": "high", "weight": 1.0 },
    "perplexity": { "enabled": true, "priority": "medium", "weight": 0.8 },
    "google-sge": { "enabled": true, "priority": "medium", "weight": 0.9 }
  },
  "scoring": {
    "authority": { "weight": 20 },
    "entity-relationships": { "weight": 20 },
    "content-structure": { "weight": 20 },
    "data-quality": { "weight": 20 },
    "citation-density": { "weight": 10 },
    "technical-optimization": { "weight": 10 }
  },
  "thresholds": {
    "good-score": 70,
    "excellent-score": 85
  }
}
```

## 模板和资源

### 模板文件

- **ai-citation-optimization.md** - AI 引用优化详细策略
- **llm-content-structure.md** - LLM 友好内容结构模板
- **entity-relationships.md** - 实体关系构建指南

### 参考资源

- **ai-search-engines.md** - AI 搜索引擎特性详解
- **citation-patterns.md** - 引用模式分析指南

### 文档

- **geo-optimization.md** - GEO 完整指南
- **geo-best-practices.md** - GEO 最佳实践

## 数据存储

### 报告数据

```
.claude-flow/cache/reports/geo/
├── audit-20240115.json
├── entities-20240115.json
├── citation-monitor-20240215.json
└── competitor-compare-20240215.json
```

### 历史数据

```
.claude-flow/cache/history/geo/
├── 2024-01.json
├── 2024-02.json
└── 2024-03.json
```

## 与传统 SEO 的关系

### 协同作用

GEO 和传统 SEO 不是互相替代，而是相互补充：

**传统 SEO 优势：**
- Google、Bing 等传统搜索引擎
- 基于链接和排名信号
- 需要积累权威性
- 见效时间 3-6 个月

**GEO 优势：**
- ChatGPT、Claude、Perplexity、Google SGE
- 基于内容质量和理解
- 一旦被学习相对稳定
- 可能更快见效（1-3 个月）

**最佳策略：**
- 同时优化传统 SEO 和 GEO
- 共享内容优化努力
- 全面覆盖所有搜索渠道
- 预计未来：传统 SEO 60-70% + GEO 30-40%

## 技术要求

### 必需工具

- Claude Code CLI
- Node.js (可选，用于高级功能)
- 文本编辑器（Markdown 编辑）

### 推荐工具

- **Schema 验证：** https://validator.schema.org
- **页面速度测试：** https://pagespeed.web.dev
- **移动友好测试：** https://search.google.com/test/mobile-friendly
- **结构化数据测试：** https://search.google.com/test/rich-results

## 支持和帮助

### 文档资源

- [GEO 优化指南](../docs/geo-optimization.md)
- [GEO 最佳实践](../docs/geo-best-practices.md)
- [AI 搜索引擎特性](../skills/geo-optimizer/resources/ai-search-engines.md)
- [引用模式分析](../skills/geo-optimizer/resources/citation-patterns.md)

### 常见问题

**Q: GEO 会取代传统 SEO 吗？**
A: 不会。GEO 是传统 SEO 的补充，最佳策略是同时优化两者。

**Q: GEO 需要多长时间见效？**
A: 通常 1-3 个月，比传统 SEO 可能更快。

**Q: 如何测量 GEO 效果？**
A: 使用 `/geo-citation-monitor` 和 `/geo-visibility-report` 命令。

**Q: GEO 适合所有类型的内容吗？**
A: GEO 特别适合教育、指南、研究、工具推荐等内容。

## 贡献和反馈

### 问题报告

如果遇到问题或有建议，请通过以下方式反馈：
- GitHub Issues
- 邮件反馈
- 社区讨论

### 贡献指南

欢迎贡献以下内容：
- 新的优化策略和模板
- 案例研究和成功故事
- 工具和资源推荐
- 文档改进

## 版本历史

### v1.0.0 (2024-01-15)
- ✅ 初始版本发布
- ✅ 核心 6 维度评分系统
- ✅ 5 个 GEO 命令
- ✅ 完整的模板和资源
- ✅ 双语支持（中文/英文）

---

**系统版本：** 1.0.0
**最后更新：** 2024-01-15
**维护者：** Claude Code SEO Assistant Team

**许可协议：** MIT License
