from ollama import chat

response = chat(
    model= "llama3.2",
    messages={
        {
            role":"user",
            "context":"write me a whatsapp message to my friend srisai asking her to meet me at the bus stop. keep the answer under 2 lines"
        }"
    }
)
print(response.message.content)
