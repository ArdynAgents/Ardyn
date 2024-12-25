import unittest
from core.learning import Learning

class TestLearning(unittest.TestCase):
    def test_reinforce(self):
        learning = Learning()
        learning.reinforce("New Data")
        self.assertIn("New Data", learning.knowledge)
