import unittest
from core.behavior import Behavior

class TestBehavior(unittest.TestCase):
    def test_adapt_behavior(self):
        behavior = Behavior()
        behavior.adapt_behavior()
        self.assertEqual(behavior.state, "Active")
