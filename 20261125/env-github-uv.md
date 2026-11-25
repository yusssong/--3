重新学习环境管理 conda训练可以，开发不行    github- uv





安装ollama框架https://ollama.com/download

用来运行大模型的



查看下载的大模型

```
ollama ps
```



```
ollama list
```



![image-20261125112858764](C:\Users\Student\AppData\Roaming\Typora\typora-user-images\image-20261125112858764.png)

模型选择，大概根据显存来估计一下，显存不够的话cpu来凑

```
ollamae run qwen3.5:4b
```

![image-20261125114036578](C:\Users\Student\AppData\Roaming\Typora\typora-user-images\image-20261125114036578.png)



openai需要在项目目录 下cmd然后在下载



kpi密钥-[大模型服务平台百炼控制台](https://bailian.console.aliyun.com/cn-beijing/model/market/detail/qwen4-max?serviceSite=asia-pacific-china&ref=list)

```
sk-ws-H.XDMIIPY.Wuj0.MEQCIHUdRxC3SpPuPSToZWmdZaPVWerP5ai6EyfPGIHK3DJBAiAoF_7qAEwQmcPRMR-Aw5bzazohAU1UBiCOLJU-koXR8A
```

示例代码

```
from openai import OpenAI
import os

client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://ws-t4tblupr780k939c.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)

messages = [{"role": "user", "content": "你是谁"}]
completion = client.chat.completions.create(
    model="qwen4-max",  # 您可以按需更换为其它深度思考模型
    messages=messages,
    extra_body={"enable_thinking": True},
    stream=True
)
is_answering = False  # 是否进入回复阶段
print("\n" + "=" * 20 + "思考过程" + "=" * 20)
for chunk in completion:
    if not chunk.choices:
        continue
    delta = chunk.choices[0].delta
    if hasattr(delta, "reasoning_content") and delta.reasoning_content is not None:
        if not is_answering:
            print(delta.reasoning_content, end="", flush=True)
    if hasattr(delta, "content") and delta.content:
        if not is_answering:
            print("\n" + "=" * 20 + "完整回复" + "=" * 20)
            is_answering = True
        print(delta.content, end="", flush=True)
```



下午



安装

```
uv pip install langchain
uv pip install openai
uv pip install ollama
uv pip install langchain-ollama
uv pip install langchain-openai
```





把环境配好

ollama配好

uv熟练些，模型调用起来



建议 自己去创建一个github库（尽量）





上班三件套

git

docker

fastapi