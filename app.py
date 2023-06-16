import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
from dotenv import load_dotenv
load_dotenv()
import os

# os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

email_template = """
Write an email to {addressed_to} with the subject {subject} in {tone} tone.
"""

email_prompt = PromptTemplate(template = email_template, input_variables = ['addressed_to', 'subject', 'tone'])

gpt3_model = OpenAI(model_name = "text-davinci-003", temperature = 1)

email_generator = LLMChain(prompt = email_prompt, llm = gpt3_model)

st.title("Email Generator 📨")
st.subheader("🚀 Generate emails on the go!")

addressed_to = st.text_input("Whom do you want to send the email to?")
subject = st.text_input("Subject of email")
tone = st.selectbox("Tone", ["Formal", "Informal"])



if st.button("Generate"):
    email = email_generator.run(addressed_to = addressed_to, subject = subject, tone = tone)
    st.write(email)
