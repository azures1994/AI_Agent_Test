from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-plus", api_key="sk-0e3d33286192466e8602460cbc976ce3")

prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname}, 刚生了{gender}, 你帮我起个名字, 简单回答, 请推荐是个名字以供选择。"
)

#! 标准写法
# prompt_text = prompt_template.format(lastname="丘", gender="女儿")
# res = model.invoke(input=prompt_text)
# print(res)

#! 基于chain链的写法
chain = prompt_template | model
res = chain.invoke(input={"lastname": "丘", "gender": "女孩"})
print(res)
