from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv  

load_dotenv()

model=ChatOpenRouter(model="minimax/minimax-m2.7:free",
                     temperature=1)

messages=[
    SystemMessage(content="You are a doctor"),
    HumanMessage(content="Tell me about cpr")
]

resukt=model.invoke(messages)

messages.append(AIMessage(content=resukt.content))
print(messages)

