from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-plus", api_key="sk-0e3d33286192466e8602460cbc976ce3")

# invoke方法：一次性返回完整结果
# res = model.invoke(input="使用Pytorch框架写一个MobileNetV3的网络结构。")
# print(res)

# stream方法：逐段返回结果，流式输出
res = model.stream(input="使用Pytorch框架写一个MobileNetV3的网络结构。")
for chunk in res:
    print(chunk, end="", flush=True)
