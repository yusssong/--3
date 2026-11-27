##提示词模板



#PromptTemplate
from langchain_core.prompts import PromptTemplate

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="qwen4-max",api_key="sk-ws-H.XDMHYIE.cZDL.MEYCIQC-L2wL9pNNiogCoWU9JQxkR-erjWbUuH_JIeOKTXz3NAIhAPzDFPYDniB01K56pbgHtFWf_UePuUd4nSlBlbpriOQp",base_url="https://cn-beijing.maas.qianwenaiapi.com/compatible-mode/v1",
                    temperature=1.2,
                    top_p=0.9,
                    extra_body={"enable_thinking": False}
                   )


#PromptTemplate


# template = "给我讲一个{adjective}的关于{content}的笑话。"



# multiple_input_prompt = PromptTemplate(
#     input_variables=["adjective", "content"], 
#     template= template
# )


# res = multiple_input_prompt.invoke({"adjective": "有趣的", "content": "足球"})

# print(res.to_messages())



# res2 = model.invoke(res.to_messages)
# print(res2.content)




#ChatPromptTemplate

from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain.messages import HumanMessage,AIMessage


prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个{job}助手，你的语言风格很幽默，可以参考郭德纲的语言风格，可以适当使用网络流行语。"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "用户输入：{user_input}")
])



messages_dict = {'user_id_1': [], 'user_id_2': []}


while True:
    user_input = input("请输入：")
    user_id = input("请输入用户ID：")
    prompt_value = prompt.invoke({"job": "聊天", "user_input": user_input, "chat_history": messages_dict[user_id]})
    messages_dict[user_id].append(HumanMessage(content=user_input))
    res = model.invoke(prompt_value)
    messages_dict[user_id].append(res)
    print(res.content)
   