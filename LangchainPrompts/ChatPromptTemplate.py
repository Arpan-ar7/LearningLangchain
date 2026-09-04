from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

load_dotenv()


model=ChatOpenRouter(model="minimax/minimax-m2.7:free")

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} expert"),
    ("human", "Explain in simple terms, what is {topic}")
])
prompt = chat_template.invoke({
    "domain": "cricket",
    "topic": "DHONI"
})

print(prompt)



