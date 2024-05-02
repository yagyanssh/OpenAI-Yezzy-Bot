from openai import OpenAI

client = OpenAI(api_key="API_KEY")

# Set up your API key

# Set up the prompt and parameters
prompt = "What is One Piece?"
model = "gpt-3.5-turbo-instruct"
temperature = 0.7
max_tokens = 100

# Generate text using OpenAI's GPT-3
response = client.completions.create(
    model=model,  # Use 'model' instead of 'engine'
    prompt=prompt,
    stream=None,
    temperature=temperature, 
    max_tokens=max_tokens
)


# Print the generated text
print(response.choices[0].text.strip())
