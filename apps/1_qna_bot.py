# from dotenv import load_dotenv
# load_dotenv()
from langchain_ollama import ChatOllama
import streamlit as st

llm=ChatOllama(
    model="qwen3:14b",
    temperature=0
)
st.title("🤖 ASK AI QNA BOT")
st.markdown("My QNA bot with langchain & ollana qwen3 model")

if "messages" not in st.session_state: # messages is key for storing session storage in streamlit server, sim to localstorage in fe
    st.session_state.messages=[] # going to list of dict

for msg in st.session_state.messages:
    role=msg["role"]
    content=msg["content"]
    st.chat_message(role).markdown(content) # 1 user input and 1 ai output/response

query=st.chat_input("Ask anything?") # input/text input box
if query:
    # print(query)
    st.session_state.messages.append({"role":"user","content":query})
    st.chat_message("user").markdown(query) # output
    res=llm.invoke(query)
    st.chat_message("ai").markdown(res.content)
    st.session_state.messages.append({"role": "ai", "content": res.content})

# while True:
#     que=input("user: ")
#     if que.lower() in ["exit","quit","bye"]:
#         break;
#     res=llm.invoke(que)
#     print(res.content