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

