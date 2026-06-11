import threading
from models import Book, Author, Reader
from library import LibraryDatabase

def main():
    print("--- Ініціалізація бази даних та об'єктів ---")
    db = LibraryDatabase()

    # Створення даних
    author1 = Author("Джордж Орвелл")
    book1 = Book("1984", author1)
    book2 = Book("Колгосп тварин", author1)

    db.add_book(book1)
    db.add_book(book2)

    reader1 = Reader("Олексій")
    reader2 = Reader("Іван")

    db.register_reader(reader1)
    db.register_reader(reader2)

    print("\n--- Тестування обробки виключень (Валідація) ---")
    try:
        invalid_book = Book("", author1)
    except ValueError as e:
        print(f"[ПЕРЕХОПЛЕНО ВИКЛЮЧЕННЯ] {e}")

    print("\n--- Тестування мультипоточних запитів ---")
    # Створюємо два потоки, які одночасно намагаються взяти ОДНУ й ТУ САМУ книгу
    thread1 = threading.Thread(target=db.borrow_book_thread, args=(reader1, "1984"), name="Потік-1")
    thread2 = threading.Thread(target=db.borrow_book_thread, args=(reader2, "1984"), name="Потік-2")

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("\n--- Фінальний стан доступності книг ---")
    print(f"Книга '1984' доступна: {book1.is_available}")

if __name__ == "__main__":
    main()
