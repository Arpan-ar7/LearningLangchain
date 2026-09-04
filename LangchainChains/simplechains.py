from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt=PromptTemplate(
    template="Generate 5 imp facts about{topic}",
    input_variables=['topic']
)

model=ChatOpenRouter(model="nvidia/nemotron-3.5-lightning:free")

parser=StrOutputParser()

chain=prompt | model | parser       

result=chain.invoke({'topic':'football'})

# print(result)

chain.get_graph().print_ascii()