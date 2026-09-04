from langchain_core.prompts import PromptTemplate
from langchain_openrouter import ChatOpenRouter
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="zai-org/GLM-5.3-Flash",
    task="text-generation"
)


model=ChatOpenRouter(model="inclusionai/ling-3.0-flash-fin:free")
model2=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

prompt1=PromptTemplate(
    template="Generate short and simple notes from the following text .\n {text}",
    input_variables=['text']
)

prompt2=PromptTemplate(
    template="Generate 3 mcq questions from the following text \n {text}",
    input_variables=['text']
)
prompt3=PromptTemplate(
    template="Now merge the notes and quize into a single doc \n -> {notes} \n {mcq} ",
    input_variables=['notes','mcq']
)

parallel_chain=RunnableParallel(
    {
        'notes': prompt1 | model | parser,
        'mcq': prompt2 | model2 | parser,

    }
)

merge_chain=    prompt3 | model2 | parser 

chain =parallel_chain | merge_chain

text="""The Transformer architecture is a deep learning architecture that was introduced in the research paper “Attention Is All You Need” in 2017. It was originally designed for machine translation but quickly became one of the most important architectures in Natural Language Processing. Unlike traditional RNNs and LSTMs, Transformers do not process words one by one. Instead, they can process the entire sequence in parallel, which makes training much faster and allows the model to learn relationships between words that may be far apart in a sentence.

The core idea behind the Transformer is the attention mechanism, particularly self-attention. Self-attention allows each token in a sentence to look at other tokens and determine which ones are important for understanding its meaning. For example, in the sentence “The animal did not cross the road because it was tired,” the model needs to understand that “it” refers to the animal. Attention helps the model establish such relationships. To calculate attention, every token is converted into three vectors called Query, Key, and Value. The Query represents what information a token is looking for, the Key represents the information available for matching, and the Value contains the information that will be passed to the next layer.

The original Transformer consists of two major parts: an encoder and a decoder. The encoder receives the input sequence and creates meaningful representations of the input. The decoder uses these representations to generate the output sequence. Before entering the Transformer layers, text is converted into tokens, and each token is represented using an embedding vector. Since Transformers do not naturally understand the order of tokens, positional encoding is added to provide information about the position of each token in the sequence.

The encoder contains multiple layers, and each layer includes multi-head self-attention and a feed-forward neural network. Multi-head attention allows the model to focus on different relationships between tokens at the same time. After the attention operation, the result passes through a feed-forward neural network. Transformers also use residual connections and layer normalization, which help make the training process more stable and effective. The decoder has similar components but also includes mechanisms that allow it to use information from the encoder when generating the output.

Modern Transformer-based models are often built using only specific parts of the original architecture. For example, BERT primarily uses the encoder portion, while GPT primarily uses the decoder portion. Decoder-only models are especially popular for text generation because they predict the next token based on the tokens that came before it. Transformers have become the foundation of many modern AI systems and large language models because they can efficiently process large amounts of data and learn complex relationships between tokens. Today, Transformer architectures are used not only in language models but also in computer vision, speech processing, multimodal AI, and many other areas of artificial intelligence."""

result=chain.invoke({'text':text})

print(result)

# chain.get_graph().print_ascii() # to visualize hte graph how things work
