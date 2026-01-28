from typing import Any, List, Optional
from langchain_core.language_models import LLM
import requests

class INF3995LLM(LLM):
    api_url: str
    api_key: str
    headers: dict

    def __init__(self, api_url: str, api_key: str, **kwargs):
        headers = {
            "x-api-key": api_key
        }
        super().__init__(api_url=api_url.rstrip('/'), api_key=api_key, headers=headers, **kwargs)
    
    def _call(self, prompt: str, stop: Optional[List[str]] = None, **kwargs) -> str:
        # Use form data format as expected by the API
        response = requests.post(f"{self.api_url}/api/chat", headers=self.headers, data={"prompt": prompt})
        response.raise_for_status()
        return response.json()["response"]

    def _llm_type(self) -> str:
        return "inf3995-llm"

if __name__ == "__main__":
    llm = INF3995LLM(api_url="http://localhost:8000", api_key="dev_key_123")
    print(llm.invoke("What is the capital of France?"))
