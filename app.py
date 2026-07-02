from ollama import chat

with open("profile.md", "r") as f:
    profile = f.read()

SYSTEM_PROMPT = f"""
You are Dhananjay Kale's personal AI assistant.

Use the following information:

{profile}

Answer naturally.
If information is unavailable, say:
'I don't know that yet.'
"""

print("🤖 Personal AI Assistant")
print("Type 'exit' to quit.\n")

while True:
    q = input("You: ")

    if q.lower() == "exit":
        break

    response = chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": q},
        ],
    )

    print("\nAssistant:")
    print(response["message"]["content"])
    print()
