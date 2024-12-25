import unittest
from core.agent import Agent

class TestAgent(unittest.TestCase):
    def test_agent_initialization(self):
        agent = Agent(name="TestAgent")
        self.assertEqual(agent.name, "TestAgent")
