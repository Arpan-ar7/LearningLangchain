from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenRouter(
    model="minimax/minimax-m3:free",
    # temperature=0.9,
    max_completion_tokens=20
)

response = model.invoke(
    "WHAT IS SPACE"
)

print(response.content) #use .content to print only the ans