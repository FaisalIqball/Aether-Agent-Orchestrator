import logging
from typing import List, Dict, Any
from .agent import Agent
from .state import State

class Orchestrator:
    """The central brain that manages multi-agent workflows."""
    
    def __init__(self, agents: List[Agent], config: Dict[str, Any] = None):
        self.agents = {a.name: a for a in agents}
        self.config = config or {}
        self.logger = logging.getLogger("Aether.Orchestrator")

    def run(self, task: str) -> State:
        self.logger.info(f"Starting task: {task}")
        state = State(input=task)
        
        # Simple linear flow for demonstration; production uses graph transitions
        for agent_name, agent in self.agents.items():
            self.logger.info(f"Invoking agent: {agent_name}")
            output = agent.process(state)
            state.update(agent_name, output)
            
        return state
