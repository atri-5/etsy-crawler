thonimport json

class DataExporter:
    def __init__(self):
        pass
    
    def export(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)