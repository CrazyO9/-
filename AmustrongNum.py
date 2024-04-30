try:
    userInput = input("Entriy your number(3 digits): ")
    left = userInput[0]
    mid = userInput[1]
    right = userInput[2]
    total = int(left)**3 + int(mid)**3 + int(right)**3
    intConn = int(userInput)
    print(f'ur Num: {userInput}')
    print(f'Total: {total}')
    if total == intConn:
        print("Is amustrong num")
    else:
        print("Not amustrong num")
except Exception as e:
    if "index out" in str(e):
        print("Amustrong number is 3 digits.")