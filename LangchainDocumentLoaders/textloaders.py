from langchain_community.document_loaders import TextLoader
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatOpenRouter(model="inclusionai/ling-3.0-flash-fin:free")

prompt=PromptTemplate(
    template='summary for the following poems ' \
    '{poem}',
    input_variables=['poem']
)
parser=StrOutputParser()
loader=TextLoader('LangchainDocumentLoaders/Poem.txt',encoding='utf-8')

docs=loader.load()

chain = prompt | model | parser

result=chain.invoke({'poem':docs[0].page_content})

print(result)