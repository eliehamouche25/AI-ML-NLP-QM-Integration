
import unittest
from nlp.nlp_module import NLPModule

class TestNLPModule(unittest.TestCase):
    def setUp(self):
        self.nlp_module = NLPModule("TestNLP")

    def test_entity_extraction(self):
        text = "Elie created a Framework for Humanity"
        result = self.nlp_module.process_text(text)
        self.assertGreater(len(result), 0)
        self.assertTrue(any(e.entity_type == "ProperNoun" for e in result))

if __name__ == "__main__":
    unittest.main()

    