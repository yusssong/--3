#模型调用


from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="qwen4-max",api_key="sk-ws-H.XDMHYIE.cZDL.MEYCIQC-L2wL9pNNiogCoWU9JQxkR-erjWbUuH_JIeOKTXz3NAIhAPzDFPYDniB01K56pbgHtFWf_UePuUd4nSlBlbpriOQp",base_url="https://cn-beijing.maas.qianwenaiapi.com/compatible-mode/v1",
                    temperature=1.2,
                    top_p=0.9,
                    extra_body={"enable_thinking": False}
                   )

# top_p,temperature, 控制输出的随机性的参数。  

prompt = """

样例/背景/上下文：
心安身自安，身安室自宽。
心与身俱安，何事能相干。
谁谓一身小，其安若泰山。
谁谓一室小，宽如天地间。

用户输入：请帮我写一首诗，主题是大雾，风格类似于李白

输出格式：必须以json格式输出，输出格式为：
{
    "诗句": "诗句",
    "解释": "解释",
    "出处": "出处",
    "赏析": "赏析"
}
"""

res = model.invoke(prompt)
print(res.content)