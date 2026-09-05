from langchain_community.document_loaders import WebBaseLoader
url="https://openrouter.ai/inclusionai/ling-3.0-flash-fin:free"
loader=WebBaseLoader(
url
)

docs=loader.load()

print(docs)