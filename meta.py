import functools

# Метаклас для логування створення об'єктів
class LogMeta(type):
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        print(f"[LOG] Створено об'єкт класу {cls.__name__} з аргументами: {args} {kwargs}")
        return instance

# Декоратор для валідації рядків (наприклад, ім'я чи назва не порожні)
def validate_string(func):
    @functools.wraps(func)
    def wrapper(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Помилка валідації: значення має бути непустим рядком.")
        return func(self, value)
    return wrapper
