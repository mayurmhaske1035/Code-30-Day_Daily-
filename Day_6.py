def even_number(no):
    for i in range (0,no+1):
        if i%2==0:
            yield i

even_number(10)
for i in even_number(10):
    print(i)
