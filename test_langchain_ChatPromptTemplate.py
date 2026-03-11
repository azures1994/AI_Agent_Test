from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi

chat = ChatTongyi(model="qwen-plus", api_key="sk-0e3d33286192466e8602460cbc976ce3")

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你一位来自边塞的诗人。"),
        MessagesPlaceholder("history"),
        ("human", "再给我写一首唐诗吧")
    ]
)

history_data = [
    ("human", "给我写一首唐诗吧"),
    ("ai", "床前明月光，疑是地上霜。举头望明月，低头思故乡。"),
    ("human", "好诗好诗，再给我写一首唐诗吧"),
    ("ai", "白日依山尽，黄河入海流。欲穷千里目，更上一层楼。")
]

chat_prompt_text = chat_prompt_template.invoke(input={"history": history_data}).to_string()
print(chat_prompt_text)

res = chat.invoke(input=chat_prompt_text)
print(res.content)