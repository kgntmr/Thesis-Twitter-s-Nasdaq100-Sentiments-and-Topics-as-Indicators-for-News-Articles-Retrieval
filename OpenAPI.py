import os
import json

# Load the configuration file
with open('OpenAPI.json', 'r') as config_file:
    config = json.load(config_file)

# Set the environment variable
os.environ['OpenAPI'] = config['OpenAPI']

# Now you can access it as usual
api_key = os.getenv('OpenAPI')
if api_key is None:
    raise ValueError("OpenAPI is not set in the environment.")
else:
    print("OpenAPI is set successfully.")
    print(f"API Key: {api_key}")