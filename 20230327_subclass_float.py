class Distance(float):
    def __init__(self, value, unit):
        super().__init__(value)
        self.unit = unit

Distance(42.0, "Miles")