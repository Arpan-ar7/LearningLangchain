from langchain_core.output_parsers import StrOutputParser
from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenRouter(model="inclusionai/ling-3.0-flash-fin:free")

parser=StrOutputParser()

prompt1=PromptTemplate(
    template="Generate a report on {topic}",
    input_variables=["topic"]
)
prompt2=PromptTemplate(
    template="Tell me 2 importand points in one line each points7 from: \n {text}",
    input_variables=["text"]

)

chain= prompt1 | model | parser | prompt2 | model | parser

result=chain.invoke({'topic':'football'})

print(result)

# chain.get_graph().print_ascii()