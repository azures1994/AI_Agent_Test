from langchain_community.embeddings import DashScopeEmbeddings

model = DashScopeEmbeddings(dashscope_api_key="sk-0e3d33286192466e8602460cbc976ce3")

vector1 = model.embed_query("hello world")
vector2 = model.embed_documents(["hello world", "hi"])

print(vector1)
print(vector2)