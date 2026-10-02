response = chat(
    model = "llama3.2",
messages={
    {
    "role":"user"
    "content":"what is SQL? explain briefly"
    }
}
)
print(response.message.content)
