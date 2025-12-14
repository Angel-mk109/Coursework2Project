import streamlit as st

st.title('Cyber Dash')

#1. st.chat_input
#2. st.chat message

# define session state to store historical information for a given message
if 'message' not in st.session_state:
    st.session_state.message = []



# to display the historical data
for message in st.session_state.message:
    with st.chat_message('user'):
        st.markdown(message)


prompt = st.chat_input('Hello, please type your query here')
if prompt:
    st.session_state.message.append(prompt)

    with st.chat_message('user'):
        st.markdown(prompt)
