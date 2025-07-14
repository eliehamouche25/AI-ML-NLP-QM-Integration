# tests/test_aiochestrator.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from aio.aiochestrator import AIOrchestrator
from core.result import Result
from core.status import Status

class TestAIOrchestrator(unittest.TestCase):
    def setUp(self):
        self.orchestrator = AIOrchestrator()

    def test_run_pipeline(self):
        text = "OpenAI and Elie are building the future with AI."
        result, status = self.orchestrator.run_full_pipeline(text)

        self.assertTrue(status.success)
        self.assertIn("sentiment", result.content)
        self.assertIn("ml_prediction", result.content)
        self.assertIn("quantum_result", result.content)

    def test_full_pipeline(self):
        orchestrator = AIOrchestrator("MasterAI")
        result, status = orchestrator.run_full_pipeline("OpenAI and Elie are exploring quantum computing with AI.")
        self.assertTrue(status.success)
        self.assertIn("sentiment", result.content)
        self.assertIn("ml_prediction", result.content)
        self.assertIn("quantum_result", result.content)

if __name__ == "__main__":
    unittest.main()