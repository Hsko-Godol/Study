def print_list(data):
    print("list = ", end='')
    for i in range(len(data)):
        print(data[i], end=' ')
    print()

def problem_1():
    print("### The result of problem 1 ###")
    i = 0
    while i < 10:
        print("i =", i)
        i = i + 1

def problem_2():
    print("### The result of problem 2 ###")
    i = 9
    while i >= 0:
        print("i =", i)
        i = i - 1

def problem_3():
    print("### The result of problem 3 ###")
    num = 0
    while not (3 * num / 2 == 63):
        num = num + 1
    print("num =", num)

def main():
    problem_1()
    print("-----------------------------")

    problem_2()
    print("-----------------------------")

    problem_3()
    print("-----------------------------")

main()
