for i in range(2, 10):
    for j in range(2, i):
        if i % j == 0:
            print i, "equals", j, "*", i/j
            break
    # until second loop is over
    else:
        print i, "is prime number"