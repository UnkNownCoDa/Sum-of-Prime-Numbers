#Program to find the sum of prime numbers in a list

List = []
sum = 0
size = int(input("Enter number of elements: "))
for i in range(0, size):
    temp = int(input("Enter element: "))
    List.append(temp)
for i in List:
    check = 1
    for j in range(2, i):
        if i%j == 0:
            check = 0
            break
    if check == 1 and i != 1:
        sum += i
print(f"Sum of prime numbers in the list: {sum}")
