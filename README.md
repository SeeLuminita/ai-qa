# 企业知识库问答系统

基于 Streamlit + LangChain + Qdrant 的智能问答系统

## 功能特性

- 📚 支持多种文档格式：TXT、PDF、DOCX、Excel
- 🔍 RAG 智能问答
- 💾 Qdrant 向量数据库
- 🎯 可配置检索参数
- 🌐 支持本地和云端部署

## 本地开发

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

创建 `.env` 文件：

```env
# 百炼 API（必需）
DASHSCOPE_API_KEY=your_dashscope_api_key

# Qdrant 本地模式（默认）
QDRANT_URL=http://localhost:6333

# Qdrant Cloud 模式（可选）
# QDRANT_URL=https://your-cluster-url.qdrant.io
# QDRANT_API_KEY=your_qdrant_api_key
```

### 3. 启动 Qdrant（本地模式）

```bash
# 使用 Docker
docker run -p 6333:6333 qdrant/qdrant

# 或下载二进制文件运行
# https://github.com/qdrant/qdrant/releases
```

### 4. 运行应用

```bash
streamlit run knowledge.py
```

## Streamlit Cloud 部署

### 方案 1: 使用 Qdrant Cloud（推荐）

1. **注册 Qdrant Cloud**
   - 访问：https://cloud.qdrant.io/
   - 免费套餐：1GB 存储，足够小型应用

2. **创建集群**
   - 创建免费集群
   - 获取 URL 和 API Key

3. **配置 Streamlit Cloud 环境变量**
   ```
   DASHSCOPE_API_KEY=your_dashscope_api_key
   QDRANT_URL=https://your-cluster-url.qdrant.io
   QDRANT_API_KEY=your_qdrant_api_key
   ```

### 方案 2: 使用其他云向量数据库

如果不想使用 Qdrant Cloud，可以替换为：
- **Pinecone**：免费套餐
- **Weaviate Cloud**：免费试用
- **Chroma**：使用 Streamlit 的文件存储（需修改代码）

## 使用说明

1. 上传文档（支持多文件）
2. 选择构建方式：
   - **增量添加**：保留已有文档，追加新文档
   - **清空重建**：删除所有旧文档，重新构建
3. 点击"构建知识库"
4. 在对话框中提问

## 检索参数说明

- **相似度优先**：返回最相关的 k 个文档
- **阈值过滤**：只返回相似度超过阈值的结果
- **距离阈值**：距离越小越相似，阈值越小越严格

## 技术栈

- **前端**：Streamlit
- **LLM**：阿里云百炼（通义千问）
- **Embedding**：百炼 text-embedding-v3
- **向量数据库**：Qdrant
- **框架**：LangChain

## 注意事项

- 百炼 Embedding API 每次最多处理 10 个文本
- 文档分割参数：chunk_size=500, chunk_overlap=100
- 支持 Qdrant 本地服务器和云端两种部署模式
