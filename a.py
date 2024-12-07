import openai

openai.api_key = "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"

try:
    response = openai.Model.list()
    print("API Key is valid:", response)
except openai.AuthenticationError as e:
    print("Authentication Error:", e)
