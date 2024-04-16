# Azure OpenAI Retry Mechanism
This workspace contains a Python script (`retry.py`) that demonstrates how to implement a retry mechanism when interacting with the Azure OpenAI API. The script uses the AzureOpenAI client to make requests to the API and handles rate limit exceeded errors (HTTP status code 429) by either switching to a different model or retrying after a specified wait time.

## Getting Started
### Prerequisites
 - Python 3.6 or later
 - An Azure account with an active OpenAI subscription
 - The AzureOpenAI Python SDK
### Installation
1. Clone this repository to your local machine.
2. Install the required Python packages using pip:
```python
pip install openai
```
### Configuration
You need to set the following environment variables:

 - `AZURE_OPENAI_ENDPOINT`: The endpoint for your Azure OpenAI service.
 - `AZURE_OPENAI_API_KEY`: The API key for your Azure OpenAI service.
You can set these environment variables in your shell, or you can add them to a `.env` file in the root of the project.

### Usage
Run the retry.py script:
```python
python retry.py
```
The script will make a request to the Azure OpenAI API using the `gpt-4-ptu` model. If the rate limit is exceeded, it will either switch to the `gpt-4-paygo` model or wait for a specified duration before retrying the request.