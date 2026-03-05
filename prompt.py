#PromptTemplate(Regular)
pip install langchain
import langchain
import langchain_core
from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate(template = "explain me about {topic} clearly", input_variable = ["topic"] )

prompt.format(topic = "DeepLearning")

prompt = PromptTemplate(template = "explain me about {topic} clearly in {mins}", input_variable = ["topic"], partial_variables = {"mins": 1} )

prompt.format(topic = "DeepLearning")

prompt = PromptTemplate(template = "explain me about {topic} clearly in {mins}", input_variable = ["topic"], partial_variables = {"mins": 1}, input_types = {"topic":str,"mins":int } )

from google.colab import userdata
gem = userdata.get('gemininb')

import os

os.environ["GOOGLE_API_KEY"] = gem

!pip install -U langchain-google-genai

import langchain
from langchain_google_genai import GoogleGenerativeAI, ChatGoogleGenerativeAI

model  = GoogleGenerativeAI(model = "models/gemini-flash-lite-latest", temperature = 0.3)

prompt.format(topic = "DeepLearning")

model.invoke(prompt.format(topic = "DeepLearning"))
