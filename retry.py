import os
import time
from openai import AzureOpenAI

messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
            {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
            {"role": "user", "content": "Do other Azure AI services support this too?"}
        ]

def make_request_with_retries():
    # Initialize your AzureOpenAI client
    client = AzureOpenAI(
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version="2024-02-01", # This is the most recent API version at the time this code was written.
        max_retries=5,  # Set your desired maximum number of retries
    )

    # Make the initial request to provisioned throughput deployment named = "gpt-4-ptu"
    response = client.chat.completions.create(
        model="gpt-4-ptu",
        messages=messages
    )

    # Check if the response status code is 429 (rate limit exceeded)
    if response.status_code == 429:
        # Extract the "retry-after-ms" value (in milliseconds) from the response headers
        retry_after_ms = int(response.headers.get("retry-after-ms", 5000))  # Default to 5000 ms

        # If the wait time exceeds 5000 ms, switch to Standard, Pay-as-you-go model deployment named = "gpt-4-paygo"
        if retry_after_ms > 5000:
            response = client.chat.completions.create(
                model="gpt-4-paygo",
                messages=messages
            )
        else:
            # Wait for the specified duration
            time.sleep(retry_after_ms / 1000)  # Convert milliseconds to seconds

            # Retry with the initial "gpt-4" model
            return make_request_with_retries()

    # If the response is successful (status code 200), return the result
    return response.model_dump_json()

# Example usage
result = make_request_with_retries()
print(result)
