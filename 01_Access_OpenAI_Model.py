
from openai import OpenAI

client = OpenAI(api_key="Your OpenAI key , retain double quotes")

# Execute the code block
response = client.completions.create(
model="davinci-002",
prompt="Bangalore is the capital of  ",
temperature=0.7,
max_tokens=200
)

print(response.choices[0].text.strip())
    