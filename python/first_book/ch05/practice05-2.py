def print_list(data, cnt):
    print("list = ", end='')
    for i in range(cnt):
        print(data[i], end=' ')
    print()

def problem_1():
    print("### The result of problem 1 ###")
    st = [1, 2, 3, 4, 5]
    print("Before")
    print_list(st, 5)
    st[1:4] = [3]
    print("After")
    print_list(st, 3)

def problem_2():
    print("### The result of problem 2 ###")
    st = [1, 2, 3, 4, 5]
    print("Before")
    print_list(st, 5)
    st[2:4] = [3, 3.5, 4]
    print("After")
    print_list(st, 6)

def problem_3():
    print("### The result of problem 3 ###")
    st = [1, 2, 3, 4, 5]
    print("Before")
    print_list(st, 5)
    st[1:4] = []
    print("After")
    print_list(st, 2)

def problem_4():
    print("### The result of problem 4 ###")
    st = [1, 2, 3, 4, 5]
    print("Before")
    print_list(st, 5)
    st[:] = []
    print("After")
    print_list(st, 0)

def problem_5():
    print("### The result of problem 5 ###")
    st = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Before")
    print_list(st, 10)
    nt = st[0:10:2]
    print("After")
    print_list(nt, 5)

def problem_6():
    print("### The result of problem 6 ###")
    st = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Before")
    print_list(st, 10)
    nt = st[1:10:2]
    print("After")
    print_list(nt, 5)

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

    problem_6()
    print("-----------------------------")

main()
