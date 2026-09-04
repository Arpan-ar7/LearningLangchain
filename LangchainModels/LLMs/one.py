
# These ar old do not use this in mordern projects here we are using chAT THOUGH CHATOPENROUTTER WE CAN CLICK AND CHEK THE CLASS 

from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenRouter(
    model="minimax/minimax-m3:free"
)

response = model.invoke(
    "WHAT IS 2+2"
)

print(response.content)