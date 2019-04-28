def problem_1():
    print("### The result of problem 1 ###")
    st = [1, 2, 3, 4]
    for i in range(4):
        print(st[i])

def problem_2():
    print("### The result of problem 2 ###")
    st = [1, 2, 3, 4]
    for i in range(-4, 0):
        print(st[i])

def problem_3():
    print("### The result of problem 3 ###")
    st = [1, 2, 3, 4]
    for i in range(4):
        st[i] += 1
        print(st[i])

def problem_4():
    print("### The result of problem 3 ###")
    st = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(10):
        st[i] += 1
        print(st[i])

def problem_5():
    print("### The result of problem 3 ###")
    st = [1, 2, 3, 4, 5]
    print("st =", end = ' ')
    for i in range(5):
        print(st[i], end = ' ')
    print()
    st[0], st[-1] = st[-1], st[0]
    print("st =", end=' ')
    for i in range(5):
        print(st[i], end=' ')
    print()

def main():
    problem_1()
    print("-----------------------------")

    problem_2()
    print("-----------------------------")

    problem_3()
    print("-----------------------------")

    problem_4()
    print("-----------------------------")

    problem_5()
    print("-----------------------------")

main()
