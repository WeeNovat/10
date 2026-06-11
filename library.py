import threading
import time
from models import Book, Reader

# Паттерн Singleton для системи управління бібліотекою (потокобезпечний)
class LibraryDatabase:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.books = []
                cls._instance.readers = []
                cls._instance.db_lock = threading.Lock() # Лок для мультипоточних операцій
        return cls._instance

    def add_book(self, book: Book):
        with self.db_lock:
            self.books.append(book)

    def register_reader(self, reader: Reader):
        with self.db_lock:
            self.readers.append(reader)

    # Метод для симуляції одночасних запитів (Мультипоточність)
    def borrow_book_thread(self, reader: Reader, book_title: str):
        indent = "   " if threading.current_thread().name == "Потік-2" else ""
        print(f"{indent}[{threading.current_thread().name}] Запит від {reader.name} на книгу '{book_title}'...")
        
        with self.db_lock:
            # Симуляція невеликої затримки обробки
            time.sleep(0.5)
            
            book = next((b for b in self.books if b.title == book_title), None)
            if not book:
                print(f"{indent}[{threading.current_thread().name}] Помилка: Книгу '{book_title}' не знайдено.")
                return

            if book.is_available:
                book.is_available = False
                reader.borrowed_books.append(book)
                print(f"{indent}[{threading.current_thread().name}] Успішно! {reader.name} взяв '{book_title}'.")
            else:
                print(f"{indent}[{threading.current_thread().name}] Відмовлено: Книга '{book_title}' вже зайнята.")
