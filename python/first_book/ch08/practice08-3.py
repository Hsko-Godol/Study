def problem_1():
    print("### The result of problem 1 ###")
    for i in  range(1, 10):
        if i % 2 == 0:
            continue
        print(i, end=' ')
    print()

def problem_2():
    print("### The result of problem 2 ###")
    i = 1
    while i < 100:
        i += 1
        if i % 2 == 0 or i % 3 == 0:
            continue
        print(i, end=' ')
    print()

def problem_3():
    print("### The result of problem 3 ###")
    i = 2
    while i < 100:
        if i % 2 != 0 and i % 3 != 0:
            print(i, end=' ')
        i += 1
    print()

def main():
    problem_1()
    print("-----------------------------")

    problem_2()
    print("-----------------------------")

    problem_3()
    print("-----------------------------")

main()
