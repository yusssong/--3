from langchain_core.messages import SystemMessage, HumanMessage

from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="qwen2.5:3b",
    api_key="123",
    base_url="http://127.0.0.1:11434/v1",  # 注意这里只留一个 base_url=
    temperature=1.2,
    max_tokens=1000,
    top_p=0.9
)

messages = [
    SystemMessage(content="你是一个聊天助手，你的语言风格很幽默，可以参考郭德纲的语言风格，可以适当使用网络流行语"),
    
]

while True:
    user_input = input("请输入：")
    messages.append(HumanMessage(content=user_input))
    res = model.invoke(messages)
    messages.append(res)
    print(res.content)
    print("------------------------")