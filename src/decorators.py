def log(filename=None):
    """
    Позволяет записывать информацию о вызовах функций, включая переданные аргументы и результаты.
    Если указано имя файла, лог записывается в этот файл; иначе выводится в консоль.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            log_message = f"Function '{func.__name__}' started with args: {args}, kwargs: {kwargs}\n"

            try:
                result = func(*args, **kwargs)
                log_message += f"Function '{func.__name__}' finished successfully with result: {result}\n"
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message)
                else:
                    print(log_message)
                return result

            except Exception as e:
                log_message += f"Function '{func.__name__}' raised an exception: {type(e).__name__} with args: {args}, kwargs: {kwargs}\n"
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message)
                else:
                    print(log_message)
                raise

        return wrapper

    return decorator


@log()
def add(a, b):
    return a + b


add(2, 3)