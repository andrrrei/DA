class Incapsulator:
    def __init__(self, value = 0):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, new_number):
        self._value = new_number
