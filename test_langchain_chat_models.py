from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# 初始化模型
chat = ChatTongyi(model="qwen-plus", api_key="sk-0e3d33286192466e8602460cbc976ce3")

# 准备消息list
messages = [
    SystemMessage(content="你是一位来自边塞的诗人。"),
    HumanMessage(content="给我写一首唐诗吧")
]

# 流式输出
for chunk in chat.stream(input=messages):
    print(chunk.content, end="", flush=True)
print()