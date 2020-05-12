def do_stuff_with_number(n):
    print(n)

the_list = (1, 2, 3, 4, 5)
for i in range(10):
    try:
        print(the_list[i])
    except IndexError: 
        print('oh noes IndexError')

