def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}\nIt returned: {function(*args)}")
        function(*args)
    return wrapper

@logging_decorator
def calc_all(*args):
    res = 0
    for i in range(len(args)):
        res+=args[i]
    return res

calc_all(1,2,3)