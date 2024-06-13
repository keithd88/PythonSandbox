import functools

def run_once(original_function):
    has_run = False

    @functools.wraps(original_function)
    def wrapper():
        nonlocal has_run
        if not(has_run):
            original_function()
            has_run = True
        else:
            print("This function can no longer be executed")
    return wrapper

@run_once
def print_name():
    print("Keith")

print_name()
print_name()

# output:
# Keith
# This function can no longer be executed.



def make_pretty(func):
    # define the inner function 
    def inner():
        # add some additional behavior to decorated function
        print("***" + func() + "***")

        # call original function
        
    # return the inner function
    return inner

# define ordinary function
@make_pretty
def ordinary():
    return "I am ordinary"

# call the decorated function
ordinary()

