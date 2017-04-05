class Counter():
    def __init__(self, integer_field_value=0):
        self.integer_field_value = integer_field_value
        self.default = integer_field_value
    def add(self, number=1):
        self.integer_field_value += number
        return self.integer_field_value
    def get(self):
        return self.integer_field_value
    def reset(self):
        self.integer_field_value = self.default
        return self.integer_field_value
