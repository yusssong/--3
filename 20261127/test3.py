##提示词模板

from langchain_core.prompts import PromptTemplate

template = "给我讲一个{adjective}的关于{content}的笑话。"

multiple_input_prompt = PromptTemplate(
    input_variables=["adjective", "content"],
    template=template
)

res = multiple_input_prompt.invoke({"adjective": "有趣的", "content": "足球"})

res2 = model.invoke(res)
print(res2.content)