from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class OpenAIClient:
    _instance = None

    @staticmethod
    def get_instance():
        if OpenAIClient._instance is None:
            OpenAIClient()
        return OpenAIClient._instance

    def __init__(self):
        if OpenAIClient._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            OpenAIClient._instance = self
            self.client = OpenAI()

    def get_client(self):
        return self.client