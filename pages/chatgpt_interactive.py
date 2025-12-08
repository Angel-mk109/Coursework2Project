from openai import OpenAI

# Initialize client
client = OpenAI(api_key="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")

# Initialize conversation history
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("ChatGPT Console Chat (type 'quit' to exit)")
print("-" * 50)

while True:
    # Get user input
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    # Add user message to history
    messages.append({"role": "user", "content": user_input})

    # Get AI response
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )

    # Extract the response
    assistant_message = completion.choices[0].message.content

    # Add assistant response to history
    messages.append({"role": "assistant", "content": assistant_message})

    # Display response
    print(f"AI: {assistant_message}\n")
