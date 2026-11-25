# 需要安装 langchain ， 安装 openai ， 安装ollama ,langchain-ollama,langchain-openai
from langchain_ollama import ChatOllama

model = ChatOllama(model="qwen2.5:3b", base_url="http://localhost:11434")
res = model.invoke("你是谁")
print(res)

from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="qwen4-max",
    api_key="sk-ws-H.XDMIIPY.Wuj0.MEQCIHUdRxC3SpPuPSToZWmdZaPVWerP5ai6EyfPGIHK3DJBAiAoF_7qAEwQmcPRMR-Aw5bzazohAU1UBiCOLJU-koXR8A",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    extra_body={"enable_thinking":False}
)
res2 = model.invoke("你是谁")
print(res2)
