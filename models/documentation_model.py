import uuid

class Doc:
    def __init__(self, full_documentation):
        self.id = str(uuid.uuid4())
        self.full = full_documentation
        self.arguments = []

    def parse_documentation(self):
        #parse function name
        #parse function args
        #parse function return
        #parse function description
        pass
