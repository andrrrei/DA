class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = float(age)

    def __repr__(self):
        return f"Student({self._name}, {self._age})"

    def __str__(self):
        return f"Student {self._name} of age {self._age}"