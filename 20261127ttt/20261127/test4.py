#示例模板
from langchain_core.prompts.few_shot import FewShotPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate

# FewShotPromptTemplate


#样例要求做成字典列表
# examples = [
#     {"question": "你好吗?", "answer": "师哥，我很好"},
#     {"question": "今天周几?", "answer": "师哥，今天星期二"},
#     {"question": "天气好吗?", "answer": "师哥，是的，今天天气很好"}
# ]



# #示例模板
# example_prompt = PromptTemplate(
#     input_variables=["question", "answer"],
#     template="问题: {question}\n回答: {answer}\n"
# )


# prompt = FewShotPromptTemplate(
#     examples=examples,
#     example_prompt=example_prompt,
#     prefix="你是一个{job}的助手，总是以'师哥'开头回答问题。以下是示例：\n",
#     suffix="问题: {input}\n回答:",
#     input_variables=["input", "job"]
# )

# print(prompt.invoke({"input": "你好吗?"}))


# FewShotChatMessagePromptTemplate


examples2 = [
    {"question": "你好吗?", "answer": "师哥，我很好",'input':'你好吗?'},
    # {"question": "今天周几?", "answer": "师哥，今天星期二"},
    # {"question": "天气好吗?", "answer": "师哥，是的，今天天气很好"}
]


example_prompt2 = ChatPromptTemplate.from_messages([
    ("user", "{question}\n{input}"),
    ("assistant", "{answer}")
])

few_shot_chat_message_prompt_template = FewShotChatMessagePromptTemplate(
    examples=examples2,
    example_prompt=example_prompt2,
)


promt = ChatPromptTemplate.from_messages([
    ("system", "你是一个{job}的助手，总是以'师哥'开头回答问题。"),
    few_shot_chat_message_prompt_template,
    ("user", "{input}")
])


res = promt.invoke({"input": "你好吗?", "job": "聊天"})

print(res)
