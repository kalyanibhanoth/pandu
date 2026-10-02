from ollama import chat
bad="Tell me about cats",
good="List 3 cat breeds that are suitable for a penthouse. 2 lines about each."
responseB =chat(
    model="llama3.2",
    meassages={
        {
            "role":"user",
            "context":bad
        }
    }
)
responseG = chat(
    model="llama3.2",
    messages={
        {
            "role":"user",
            "context":good
        }
    }
)
print(f"bad prompt Result: (responseB.message.context)")
print()
print(f"good prompt Result: (responseG.message.context)")
