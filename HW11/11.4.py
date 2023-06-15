class GeomRangeIterator:
    def __init__(self, geomprogression):
        self._geomprogression = geomprogression
        self._next = self._geomprogression._start
        self._value = None

    def __next__(self):
        self._value = self._next

        if self._value < self._geomprogression._stop:
            self._next = self._next * self._geomprogression._step
            return self._value
        else:
            raise StopIteration()

    def __iter__(self):
        copy = GeomRangeIterator(self._geomprogression)
        copy._next = self._next
        return copy


class GeomRange:
    def __init__(self, start=None, stop=None, step=None):
        if stop is None:
            self._stop = start
            self._start = 1
            self._step = 2
        elif step is None:
            self._step = 2
        else:
            self._start = start
            self._stop = stop
            self._step = step

    def __getitem__(self, index):
        value = self._start

        for i in range(index):
            value = value * self._step

        if value >= self._stop:
            raise IndexError("index is out of the progression")

        return value

    def __iter__(self):
        return GeomRangeIterator(self)