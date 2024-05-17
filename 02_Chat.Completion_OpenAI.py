
# documentation can be foudn here https://platform.openai.com/docs/guides/text-generation/chat-completions-api

from openai import OpenAI

client = OpenAI(api_key="Your OpenAI key , retain double quotes")

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who is the Prime Minister of India"},
    {"role": "assistant", "content": "Narendra Modi is the Prime Minister of India"},
    {"role": "user", "content": "When is Narandra Modi'd Birthday?"}
  ]
)

print(response.choices[0].message.content.strip())


# Role "user" : It means you or who is chatting or who is asking to chat gpt.
# Role "assistant" : It means open AI(chat gpt) server - who is replying your("user" role) questions.
# Role "system" : It means the system developer who can internally give some instructions for the conversation. 
# developer can provide option for user input also which depends on the system requirements.

'''
Response is received in this format .
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "The 2020 World Series was played in Texas at Globe Life Field in Arlington.",
        "role": "assistant"
      },
      "logprobs": null
    }
  ],
  "created": 1677664795,
  "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
  "model": "gpt-3.5-turbo-0613",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 17,
    "prompt_tokens": 57,
    "total_tokens": 74
  }
}
'''

