from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="zai-org/GLM-5.3",
    task="text-generation",
    max_new_tokens=20

)
model=ChatHuggingFace(llm=llm)

result=model.invoke("Who is cristiano Ronaldo")
print(result.content)