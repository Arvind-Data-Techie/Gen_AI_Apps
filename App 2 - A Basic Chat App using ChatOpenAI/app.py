import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv


# Load the environment variables
load_dotenv()

#Function to return the response

#Uses Simple LLM Wrapper
def load_answer(question):
    chat = ChatOpenAI(temperature=.7, model='gpt-3.5-turbo')
    answer=chat(
        [
            SystemMessage(content="You are a sarcastic AI assistant"),
            HumanMessage(content=question)
        ]
    )
    return answer.content


#App UI starts here
st.set_page_config(page_title="Chat Application using Chat Open AI", page_icon=":robot:")
st.header("Chat Application using Chat Open AI")

#Gets the user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text


user_input=get_text()
response = load_answer(user_input)

submit = st.button('Generate')  

#If generate button is clicked
if submit:

    st.subheader("Answer:")

    st.write(response)

