from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from scraper import fetch_website_contents 

load_dotenv()

prompt = ChatPromptTemplate.from_template(
    "Give a short, friendly summary of this website:\n\n{website}")
model = ChatGroq(
    model_name="openai/gpt-oss-20b",
    temperature=0.3)
parser = StrOutputParser()
chain = prompt | model | parser

def summarizer(url):
    return chain.invoke({"website": fetch_website_contents(url)})

print(summarizer("https://www.wikipedia.org/"))