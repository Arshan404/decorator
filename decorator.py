from time import sleep , perf_counter

def timer(func):
    def wrapper():
        start  = perf_counter()
        func()
        run_time = perf_counter() - start
        print(f"Function {func.__name__}; took{run_time:.4f}sec.")
    return wrapper

@timer
def first():
    sleep(2)

@timer
def second():
    sleep(3)

first()
second()