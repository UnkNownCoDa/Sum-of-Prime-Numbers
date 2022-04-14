for i in range(1, 101):
    check = 1
    for j in range(2,i):
        if i%j == 0:
            check = 0
            break
    if check == 1 and i != 1:
        print(f"{i} is a prime")
    else:
        print(f"{i} is not a prime")
