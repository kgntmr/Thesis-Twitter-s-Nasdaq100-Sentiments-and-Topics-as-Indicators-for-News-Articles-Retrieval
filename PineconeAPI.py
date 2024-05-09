import os
import json

# Load the configuration file
with open('PineconeAPI.json', 'r') as config_file:
    config = json.load(config_file)

# Set the environment variable
os.environ['Pinecone_API_KEY'] = config['Pinecone_API_KEY']

# Now you can access it as usual
api_key = os.getenv('Pinecone_API_KEY')
if api_key is None:
    raise ValueError("Pinecone_API_KEY is not set in the environment.")
else:
    print("Pinecone_API_KEY is set successfully.")
    print(f"API Key: {api_key}")