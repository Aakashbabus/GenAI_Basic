from openai import OpenAI

# Set up your OpenAI API key
client = OpenAI(api_key="Your OpenAI key , retain double quotes")

def get_embeddings(text):
    """
    Generate embeddings for a given text using the OpenAI API.
    
    Args:
        text (str): The input text to generate embeddings for.
    
    Returns:
        list: The generated embeddings as a list of floats.
    """
    response = client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    
    embeddings = response.data[0].embedding
    return embeddings

# Example usage
sentence = "This is a sample sentence."
embeddings = get_embeddings(sentence)

print(f"Embeddings for '{sentence}': {embeddings}")