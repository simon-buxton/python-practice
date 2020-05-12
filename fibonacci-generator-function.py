print("hello world")

#0,1,1,2,3,5,8,13,21...
def fib():
    # for i in [0,1,1,2,3,5,8,13,21,34]:
    #     yield i

    n_previous = 1
    n_current = 1
    while True:
        sum = n_previous + n_current
        n_previous = n_current
        n_current = sum
        yield sum

    
    
import types
if type(fib()) == types.GeneratorType:
    print("The fibonacci function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 12:
            break