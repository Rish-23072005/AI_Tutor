import os
import requests
from dotenv import load_dotenv
from typing import Dict

# load env from backend/.env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

MCP_BASE = os.getenv('MCP_BASE', 'http://localhost:8001')

class MCPClient:
    def __init__(self, base_url: str = None):
        self.base = base_url or MCP_BASE.rstrip('/')

    def create_plan(self, prompt: str, params: Dict):
        """Sends a request to the MCP mock server to create a plan."""
        url = f"{self.base}/mcp/process"
        payload = {"prompt": prompt, "params": params}
        try:
            resp = requests.post(url, json=payload, timeout=5)
            resp.raise_for_status()
            data = resp.json()
            return data.get('plan', {"note":"mcp returned no plan"})
        except Exception:
            # In case MCP is down, fallback to a simple mock plan
            return {"fallback_plan": f"Summarize: {prompt[:120]}"}
