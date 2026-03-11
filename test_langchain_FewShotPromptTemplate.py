from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-plus", api_key="sk-0e3d33286192466e8602460cbc976ce3")

# 示例的模板
example_template = PromptTemplate.from_template(
    "单词：{word}, 反义词：{antonym}"
)

# 示例的动态数据注入，要求是list内部嵌套字典
example_data = [
    {"word": "快乐", "antonym": "悲伤"},
    {"word": "高兴", "antonym": "难过"},
    {"word": "大", "antonym": "小"}
]



few_shot_template = FewShotPromptTemplate(
    example_prompt=example_template,
    examples=example_data,
    prefix="告知我单词的反义词，我提供如下的示例：",
    suffix="基于前面的示例告知我，{input_word}的反义词是什么？",
    input_variables=['input_word']
)

prompt_text = few_shot_template.invoke(input={"input_word":"上窜"}).to_string()
print(prompt_text)

res = model.invoke(input=prompt_text)
print(res)