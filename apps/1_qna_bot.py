# from dotenv import load_dotenv
# load_dotenv()
from langchain_ollama import ChatOllama
import streamlit as st

llm=ChatOllama(
    model="qwen3:14b",
    temperature=0,
    reasoning=False # think=false
)
# context_window=[] # this method fails as streamlit reruns the prog and this list becomes empty

st.title("🤖 ASK AI QNA BOT")
st.markdown("My QNA bot with langchain & ollana qwen3 model")

# Initialize conversation history
if "messages" not in st.session_state: # messages is key for storing session storage in streamlit server, sim to localstorage in fe
    st.session_state.messages=[] # going to list of dict


# Display previous messages in chat
for msg in st.session_state.messages:
    role=msg["role"]
    content=msg["content"]
    st.chat_message(role).markdown(content) # 1 user input and 1 ai output/response

query=st.chat_input("Ask anything?") # input/text input box
if query:
    # print(query)
    st.session_state.messages.append({"role":"user","content":query})
    st.chat_message("user").markdown(query) # output

    # res=llm.invoke(query)
    # st.chat_message("ai").markdown(res.content)
    # st.session_state.messages.append({"role": "ai", "content": res.content})
    # AI response
    with st.chat_message("assistant"):
        response = st.write_stream(
            llm.stream(st.session_state.messages)
        )

    # Store complete streamed response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
# while True:
#     que=input("user: ")
#     if que.lower() in ["exit","quit","bye"]:
#         break;
#     res=llm.invoke(que)
#     print(res.content