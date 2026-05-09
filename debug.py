"""
调试页面 - 检查环境和依赖
"""
import streamlit as st
import sys
import os

st.title("🔍 环境诊断")

# 1. Python 版本
st.subheader("1. Python 版本")
st.code(f"Python {sys.version}")

# 2. 检查环境变量
st.subheader("2. 环境变量")
env_vars = {
    "DASHSCOPE_API_KEY": os.getenv("DASHSCOPE_API_KEY"),
    "QDRANT_URL": os.getenv("QDRANT_URL"),
    "QDRANT_API_KEY": os.getenv("QDRANT_API_KEY")
}

for key, value in env_vars.items():
    if value:
        st.success(f"✅ {key}: {'*' * 10}")
    else:
        st.warning(f"⚠️ {key}: 未设置")

# 3. 检查依赖包
st.subheader("3. 依赖包检查")

packages = [
    "streamlit",
    "langchain_openai",
    "langchain_qdrant",
    "qdrant_client",
    "dashscope",
    "pypdf",
    "docx"
]

for package in packages:
    try:
        __import__(package)
        st.success(f"✅ {package}")
    except ImportError as e:
        st.error(f"❌ {package}: {e}")

# 4. 测试 Qdrant 连接
st.subheader("4. Qdrant 连接测试")

try:
    from qdrant_client import QdrantClient
    
    qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")
    qdrant_api_key = os.getenv("QDRANT_API_KEY", None)
    
    st.info(f"连接地址: {qdrant_url}")
    
    if qdrant_api_key:
        client = QdrantClient(url=qdrant_url, api_key=qdrant_api_key)
    else:
        client = QdrantClient(url=qdrant_url)
    
    collections = client.get_collections()
    st.success(f"✅ Qdrant 连接成功！")
    st.json({
        "collections_count": len(collections.collections),
        "collections": [c.name for c in collections.collections]
    })
except Exception as e:
    st.error(f"❌ Qdrant 连接失败: {e}")

# 5. 测试百炼 API
st.subheader("5. 百炼 API 测试")

try:
    import dashscope
    from dashscope import TextEmbedding
    
    api_key = os.getenv("DASHSCOPE_API_KEY")
    if not api_key:
        st.warning("⚠️ 未设置 DASHSCOPE_API_KEY")
    else:
        dashscope.api_key = api_key
        result = TextEmbedding.call(
            model="text-embedding-v3",
            input=["测试"]
        )
        if result.output:
            st.success(f"✅ 百炼 API 正常！向量维度: {len(result.output['embeddings'][0]['embedding'])}")
        else:
            st.error(f"❌ API 返回异常: {result}")
except Exception as e:
    st.error(f"❌ 百炼 API 测试失败: {e}")

st.info("💡 如果以上检查都通过，说明环境配置正确。")
