#动态示例选择器  语义相似度示例选择器

from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_community.vectorstores import FAISS  #向量数据库


from langchain_ollama import OllamaEmbeddings #加载编码模型

from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate,ChatPromptTemplate,FewShotChatMessagePromptTemplate

# 扩展的示例数据集
more_examples = [
    {"question": "你好吗?", "answer": "师哥，我很好"},
    {"question": "今天周几?", "answer": "师哥，今天星期二"},
    {"question": "天气好吗?", "answer": "师哥，是的，今天天气很好"},
    {"question": "你叫什么?", "answer": "师哥，我是AI助手"},
    {"question": "几点了?", "answer": "师哥，我无法获取当前时间"},
    {"question": "什么是卷积神经网络", "answer": "卷积神经网络就是一个滤波器"},
    {"question": "解释一下机器学习", "answer": "师哥，机器学习是人工智能的一个分支..."},
]

# 定义示例格式化的提示模板
example_prompt = PromptTemplate(
    input_variables=["question", "answer"],
    template="问题: {question}\n回答: {answer}\n"
)


embedding_model  = OllamaEmbeddings(model="qwen3-embedding:0.6b",base_url="http://192.168.1.105:11434")  


# res = embedding_model.embed_query("你好吗?")

# print(res)

semantic_similarity_example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples=more_examples,
    embeddings=embedding_model,
    k=3,
    vectorstore_cls=FAISS,
)

semantic_prompt = FewShotPromptTemplate(
    example_selector=semantic_similarity_example_selector,
    example_prompt=example_prompt,
    prefix="基于相似问题，请回答：\n",
    suffix="问题: {input}\n回答:",
    input_variables=["input"]
)



res = semantic_prompt.invoke({"input": "你好吗?"})

print(res)

