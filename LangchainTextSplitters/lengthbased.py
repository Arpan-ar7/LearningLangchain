# from langchain_text_splitters import CharacterTextSplitter
# from langchain_community.document_loaders import PyPDFLoader

# loader=PyPDFLoader(
#     'LangchainDocumentLoaders/Sample_5_Pages.pdf'
# )


# # text = """"" The cosmos is the vast and mysterious expanse that contains everything we know: galaxies, stars, planets, moons,
# #  nebulae, black holes, and countless other objects. Our home, Earth, is part of the Solar System, which lies within the Milky Way galaxy.
# #    The universe began approximately 13.8 billion years ago with the Big Bang and has been expanding ever since. 
# #    Galaxies contain billions of stars, and many stars have planets orbiting them. Scientists study the cosmos using powerful telescopes,
# #      spacecraft, and mathematical models to understand its origins, structure, and future. Despite tremendous discoveries,
# #        much of the cosmos remains unexplored and mysterious, inspiring humanity to continue searching for answers. """

# docs=loader.load()

# splitter=CharacterTextSplitter(
#     chunk_size=100,
#     chunk_overlap=0,
#     separator=''
# )

# result=splitter.split_documents(docs)

# print(result)

# -----------------------------------------------------------------------------------

from langchain_text_splitters import RecursiveCharacterTextSplitter



text = """"" The cosmos is the vast and mysterious expanse that contains everything we know: galaxies, stars, planets, moons,
nebulae, black holes, and countless other objects. Our home, Earth, is part of the Solar System, which lies within the Milky Way galaxy.
The universe began approximately 13.8 billion years ago with the Big Bang and has been expanding ever since. 
Galaxies contain billions of stars, and many stars have planets orbiting them. Scientists study the cosmos using powerful telescopes,
spacecraft, and mathematical models to understand its origins, structure, and future. Despite tremendous discoveries,
much of the cosmos remains unexplored and mysterious, inspiring humanity to continue searching for answers. """


splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0

)
chunks=splitter.split_text(text)

print(len(chunks))