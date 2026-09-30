from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.messages import HumanMessage, AIMessage


load_dotenv()

model = ChatGroq(
    model = "openai/gpt-oss-120b"
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a professional translator.

Translate the text from {source_language}
to {target_language}.

Rules:
- Preserve the original meaning.
- Preserve the tone.
- Do not add explanations.
- Return only the translation."""
    ),
    (
        "human",
        "{text}"
    )
])

chain = prompt | model
source_languageage = input("Source language: ")
target_language = input("Target language: ")


query =  input("Enter text: ")

response = chain.invoke({"source_language":"source_languageage","target_language":target_language,"text":query})

print(response.content) 