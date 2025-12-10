import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="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")

st.title("My AI Chatbot")

# Store the chat history in Streamlit session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# User input box
user_input = st.text_input("You:", key="input")

# When the user clicks the button:
if st.button("Send"):
    if user_input:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Call the API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages
        )

        ai_message = response.choices[0].message.content

        # Save assistant message
        st.session_state.messages.append({"role": "assistant", "content": ai_message})

# Display chat messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.write(f"**You:** {message['content']}")
    elif message["role"] == "assistant":
        st.write(f"**AI:** {message['content']}")
