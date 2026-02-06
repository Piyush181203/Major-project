class CongestionPredictor:
    def __init__(self):
        # Simple rule-based for demo; replace with ML model
        self.thresholds = {"Low": 5, "Medium": 15, "High": 30}

    def predict(self, density):
        if density < self.thresholds["Low"]:
            return "Low"
        elif density < self.thresholds["Medium"]:
            return "Medium"
        else:
            return "High"
