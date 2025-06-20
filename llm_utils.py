# llm_utils.py

import os
import requests
from dotenv import load_dotenv

from IPython.display import display, Markdown

# Load environment variables from .env
load_dotenv()

class ChatBot:
    def __init__(
        self,
        provider,
        model,
        api_key=None,
        temperature=0.7,
        max_tokens=1500,
        top_p=0.9,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        min_tokens=None,
        stream=False,
        stop=None,
        random_seed=None,
        response_format=None,
        tools=None,
        tool_choice="auto",
        safe_prompt=False
    ):
        """
        Initialize the ChatBot with API key, provider, and parameters.
        
        Parameters:
        - provider (str): The LLM provider to use ("openai", "anthropic", or "mistral").
        - model (str): The model to use for text generation.
        - api_key (str, optional): The API key for the chosen provider.
        - temperature (float, optional): Controls randomness in the output.
        - max_tokens (int, optional): The maximum number of tokens to generate in the completion.
        - Additional parameters are specific to certain providers.
        """
        self.provider = provider.lower()
        self.model = model
        self.api_key = api_key or os.getenv(f"{self.provider.upper()}_API_KEY")
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.min_tokens = min_tokens
        self.stream = stream
        self.stop = stop
        self.random_seed = random_seed
        self.response_format = response_format
        self.tools = tools
        self.tool_choice = tool_choice
        self.safe_prompt = safe_prompt
        self.conversation_history = []

    def add_message(self, role, content):
        """
        Add a message to the conversation history.
        
        Parameters:
        - role (str): The role of the sender ("user" or "assistant").
        - content (str): The content of the message.
        """
        self.conversation_history.append({"role": role, "content": content})

    def _call_api(self):
        """
        Internal method to call the appropriate API based on provider and generate a response.
        
        Returns:
        - response (dict): The API response as a dictionary.
        """
        headers = {"Content-Type": "application/json"}
        if self.provider == "openai":
            url = "https://api.openai.com/v1/chat/completions"
            headers["Authorization"] = f"Bearer {self.api_key}"
            payload = {
                "model": self.model,
                "messages": self.conversation_history,
                "temperature": self.temperature,
                "max_tokens": self.max_tokens,
                "top_p": self.top_p,
                "frequency_penalty": self.frequency_penalty,
                "presence_penalty": self.presence_penalty
            }

        elif self.provider == "anthropic":
            url = "https://api.anthropic.com/v1/messages"
            headers["x-api-key"] = self.api_key
            headers["anthropic-version"] = "2023-06-01"
            payload = {
                "model": self.model,
                "temperature": self.temperature,
                "max_tokens": self.max_tokens,
                "top_p": self.top_p,
                "messages": self.conversation_history
            }

        elif self.provider == "mistral":
            url = "https://api.mistral.ai/v1/chat/completions"
            headers["Authorization"] = f"Bearer {self.api_key}"
            payload = {
                "model": self.model,
                "messages": self.conversation_history,
                "temperature": self.temperature,
                "top_p": self.top_p,
                "stream": self.stream,
                "tool_choice": self.tool_choice,
                "safe_prompt": self.safe_prompt
            }
            # Add optional parameters for Mistral
            if self.max_tokens is not None:
                payload["max_tokens"] = self.max_tokens
            if self.min_tokens is not None:
                payload["min_tokens"] = self.min_tokens
            if self.stop is not None:
                payload["stop"] = self.stop
            if self.random_seed is not None:
                payload["random_seed"] = self.random_seed
            if self.response_format is not None:
                payload["response_format"] = self.response_format
            if self.tools is not None:
                payload["tools"] = self.tools
        else:
            raise ValueError("Invalid provider. Choose from 'openai', 'anthropic', or 'mistral'.")

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def get_response(self, user_input):
        """
        Get a response from the selected provider's API based on the user input.
        
        Parameters:
        - user_input (str): The user's input message.
        
        Returns:
        - formatted_response (str): The assistant's formatted response in Markdown.
        """
        # Add user input to conversation history
        self.add_message("user", user_input)

        # Call the API to get a response
        response = self._call_api()

        if response:
            # Extract the assistant's reply based on provider
            if self.provider == "openai":
                assistant_reply = response["choices"][0]["message"]["content"]
                token_usage = response["usage"]["completion_tokens"]

            elif self.provider == "anthropic":
                assistant_reply = response.get("content", [{}])[0].get("text", "No reply found.")
                token_usage = len(assistant_reply.split())  # Estimated tokens for Anthropic

            elif self.provider == "mistral":
                assistant_reply = response.get("choices", [{}])[0].get("message", {}).get("content", "No reply found.")
                token_usage = len(assistant_reply.split())  # Estimated tokens for Mistral

            # Add assistant's reply to conversation history
            self.add_message("assistant", assistant_reply)

            # Format the response using Markdown
            formatted_response = (
                f"**Provider:** {self.provider.capitalize()} | **Model:** {self.model}  \n"
                f"**Tokens Used:** {token_usage}  \n\n"
                f"**Assistant:**\n\n{assistant_reply}\n"
            )
            return formatted_response
        else:
            return "Sorry, I couldn't generate a response."

