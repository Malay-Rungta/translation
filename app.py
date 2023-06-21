import os
from apikey import apikey
from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

llm = OpenAI(openai_api_key="OPENAI_API_KEY")

llms = OpenAI(temperature=0.9)
while (True):

    text = input("What would you like to translate? ")    
    if (text == "exit"):
        break
    destination = input("What language would you like to translate to? ")
    if (text == "exit" or destination== "exit"):
        break

    chat = "pretend you are a chatbot and answer the following: I want to translate ' "
    ending = "' from english to "
    output = chat + text + ending  + destination

    print(llms(output))