from nlp.analysis import Analysis

class NLPModule:
    def __init__(self, module_name="DefaultNLPModule"):
        self.module_name = module_name
        self.analysis = Analysis()

    def process_text(self, text: str):
        print(f"Processing text in NLPModule: {self.module_name}")
        return self.analysis.extract_entities(text)
    
     