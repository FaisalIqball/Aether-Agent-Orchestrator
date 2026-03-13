from typing import Dict, Any, List

class State:
    """Manages the global state of a workflow execution."""
    
    def __init__(self, input: str):
        self.input = input
        self.history: List[Dict[str, Any]] = []
        self.current_step = 0
        self.output = None

    def update(self, agent_name: str, result: Any):
        self.history.append({
            "agent": agent_name,
            "result": result,
            "step": self.current_step
        })
        self.current_step += 1
        self.output = result
