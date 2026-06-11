from meta import LogMeta, validate_string

class Author(metaclass=LogMeta):
    def __init__(self, name: str):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    @validate_string
    def name(self, value):
        self._name = value


class Book(metaclass=LogMeta):
    def __init__(self, title: str, author: Author):
        self.title = title
        self.author = author
        self.is_available = True

    @property
    def title(self):
        return self._title

    @title.setter
    @validate_string
    def title(self, value):
        self._title = value


class Reader(metaclass=LogMeta):
    def __init__(self, name: str):
        self.name = name
        self.borrowed_books = []

    @property
    def name(self):
        return self._name

    @name.setter
    @validate_string
    def name(self, value):
        self._name = value
