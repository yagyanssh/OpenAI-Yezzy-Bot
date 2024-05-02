from openai import OpenAI

client = OpenAI(api_key="sk-proj-MvUhkzV1dmyoPea2p0RVT3BlbkFJVe6ybMjEtOY6EYsYa7Cp")

# Set up your API key

# Set up the prompt and parameters
prompt = "What is One Piece?"
model = "text-davinci-002"
temperature = 0.7
max_tokens = 100

# Generate text using OpenAI's GPT-3
response = client.completions.create(engine=model,
prompt=prompt,
temperature=temperature, 
max_tokens=max_tokens)

# Print the generated text
print(response.choices[0].text.strip())
