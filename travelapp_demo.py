import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import streamlit as st

OPENAI_API_KEY = st.text_input("Enter your OpenAI API Key", type="password")
if not OPENAI_API_KEY:
    st.warning("Please enter your OpenAI API key to continue")
    st.stop()
llm = ChatOpenAI(model="gpt-4",api_key=OPENAI_API_KEY)

prompt_template = PromptTemplate(
    input_variables = ["city","month","language","budget"],
    template = """
    Welcome to the {city} travel guide!
    If you are visiting in {month}, then here is what you can do:
    1. Must visit attractions.
    2. Local cuisine you must try.
    3. Useful phrases in {language}.
    4. Tips for travelling on a {budget} budget.
    Enjoy your trip!
    """
)

st.title("Travel App")

city = st.text_input("Enter the city name")
month = st.text_input("Enter the month name")
language = st.text_input("Enter the language name")
budget = st.number_input("Enter the budget")
if city:
    response = llm.invoke(prompt_template.format(city=city,month=month,language=language,budget=budget))

    st.write(response.content)

