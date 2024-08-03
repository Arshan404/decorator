from time import sleep , perf_counter


def timer(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        run_time = perf_counter() - start
        print(f"Function {func.__name__}; took {run_time:.4f} sec.")
    return wrapper

def repeat(repeat_count, delay):
    def repeat_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(repeat_count):
                sleep(delay)
                func(*args, **kwargs)
        return wrapper
    return repeat_decorator

@timer
@repeat(repeat_count=2, delay=2)
def first(text):
    print(text)

@timer
@repeat(repeat_count=3, delay=1)
def second(text):
    print(text)

first("keanu")
second("matrix")
