# Menu Printing Function
a = 0
while True:
    for i in range(5):
        print(f'{i+1}')

    a = int(input('Enter Choice'))

    if a == 5:
        break
