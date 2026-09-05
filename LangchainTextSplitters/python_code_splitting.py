from langchain_text_splitters import RecursiveCharacterTextSplitter , Language

text ="""" class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

print(account.get_balance()) """

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=0
)

chunk=splitter.split_text(text)

print(len(chunk))

print(chunk[0])

