class SpyingNumber:
    operation_counter = 0

    @staticmethod
    def get_global_counter():
        return SpyingNumber.operation_counter

    @staticmethod
    def reset_global_counter():
        SpyingNumber.operation_counter = 0

    def __init__(self, value):
        self._value = value

    def __repr__(self):
        return f"SpyingNumber({self._value})"

    def __str__(self):
        return f"{self._value}"

    def __add__(self, other):
        SpyingNumber.operation_counter += 1
        if isinstance(other, (int, float)):
            other = SpyingNumber(other)

        return SpyingNumber(self._value + other._value)

    def __sub__(self, other):
        SpyingNumber.operation_counter += 1
        if isinstance(other, (int, float)):
            other = SpyingNumber(other)

        return SpyingNumber(self._value - other._value)

    def __mul__(self, other):
        SpyingNumber.operation_counter += 1
        if isinstance(other, (int, float)):
            other = SpyingNumber(other)

        return SpyingNumber(self._value * other._value)

    def __truediv__(self, other):
        SpyingNumber.operation_counter += 1
        if isinstance(other, (int, float)):
            other = SpyingNumber(other)

        return SpyingNumber(self._value / other._value)