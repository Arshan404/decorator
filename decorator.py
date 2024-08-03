from time import sleep , perf_counter
'''
def timer(func):
    def wrapper():
        start  = perf_counter()
        func()
        run_time = perf_counter() - start
        print(f"Function {func.__name__}; took{run_time:.4f}sec.")
    return wrapper
'''
def repeat(repeat_count):
    def repeat_decorator(func):
        def wrapper(*args,**kwargs):
            for i in range (repeat_count):
                func(*args , **kwargs)
            
        return wrapper
    return repeat_decorator
        
@repeat(repeat_count=2)
def first(text):
    print(text)

@repeat(repeat_count=3)
def second(text):
    print(text)

first("keanu")
second("matrix")