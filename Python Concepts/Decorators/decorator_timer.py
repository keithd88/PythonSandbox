import time

def time_function(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__!r} took {(end_time-start_time):.4f}s")
    return wrapper


@time_function
def wait_func(num):
    print(f"Waiting for {num} seconds")
    time.sleep(num)
    print("Done waiting")

wait_func(3)