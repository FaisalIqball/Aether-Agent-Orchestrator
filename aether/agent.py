from typing import Any
from .state import State

class Agent:
    """Base class for autonomous agents."""
    
    def __init__(self, name: str, role: str, model: str = "gpt-4"):
        self.name = name
        self.role = role
        self.model = model

    def process(self, state: State) -> Any:
        # In a real implementation, this would call an LLM API
        return f"Processed by {self.name} using {self.role}"
