from openai import OpenAI
import os

model_type = "qwen3.5-plus"

client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    api_key="sk-0e3d33286192466e8602460cbc976ce3",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)


# 通过 `系统(system)` 角色给 `助手(assistant)` 角色赋予一个人设
messages = [{'role': 'system', 'content': '你是一个乐于助人的诗人。'}]
# 在 messages 中加入 `用户(user)` 角色提出第 1 个问题
messages.append({'role': 'user', 'content': '作一首诗，要有风、要有肉，要有火锅、要有雾，要有美女、要有驴！'})
# 调用 API 接口
response = client.chat.completions.create(
    model=model_type,
    messages=messages,
    extra_body={"enable_thinking": False},
    # stream=True
)

# is_answering = False  # 是否进入回复阶段
# print("\n" + "=" * 20 + "思考过程" + "=" * 20)
# for chunk in response:
#     delta = chunk.choices[0].delta
#     if hasattr(delta, "reasoning_content") and delta.reasoning_content is not None:
#         if not is_answering:
#             print(delta.reasoning_content, end="", flush=True)
#     if hasattr(delta, "content") and delta.content:
#         if not is_answering:
#             print("\n" + "=" * 20 + "完整回复" + "=" * 20)
#             is_answering = True
#         print(delta.content, end="", flush=True)

# 在 messages 中加入 `助手(assistant)` 的回答
# print(response.choices[0].message.content)
messages.append({
    'role': response.choices[0].message.role,
    'content': response.choices[0].message.content,
})
# 在 messages 中加入 `用户(user)` 角色提出第 2 个问题
messages.append({'role': 'user', 'content': '好诗！好诗！'})
# 调用 API 接口

response = client.chat.completions.create(
    model=model_type,
    messages=messages,
    extra_body={"enable_thinking": False},
    # stream=True
)
# 在 messages 中加入 `助手(assistant)` 的回答
messages.append({
    'role': response.choices[0].message.role,
    'content': response.choices[0].message.content,
})
# 查看整个对话
for message in messages:
    print('\n')
    print(f"{message['role']}:\n{message['content']}")
