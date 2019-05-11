def print_list(data):
    print("list = ", end='')
    for i in range(len(data)):
        print(data[i], end=' ')
    print()

def problem_1():
    print("### The result of problem 1 ###")
    st = []
    print("First")
    print_list(st)
    st.append(1)
    st.append(2)
    st.append(3)
    print("Second")
    cnt = len(st)
    for i in range(cnt):
        print(st.pop(0), end=' ')
    print()

def problem_2():
    print("### The result of problem 2 ###")
    st = []
    print("First")
    print_list(st)
    st.append(1)
    st.append(2)
    st.append(3)
    print("Second")
    cnt = len(st)
    for i in range(cnt):
        print(st.pop(-1), end=' ')
    print()

def problem_3():
    print("### The result of problem 3 ###")
    st = [1, 2, 3, 4]
    print("Before")
    print_list(st)
    st[:] = []
    print("After")
    print_list(st)

def problem_4():
    print("### The result of problem 4 ###")
    st = []
    print("Before")
    print_list(st)
    for i in range(10):
        st.append(i+1)
    print("In progress")
    print_list(st)
    for i in range(10):
        print(st.pop(0), end=' ')
    print()
    print("After")
    print_list(st)

def problem_5():
    print("### The result of problem 5 ###")
    st = []
    print("Before")
    print_list(st)
    for i in range(10):
        st.append(i+1)
    print("In progress")
    print_list(st)
    for i in range(10):
        print(st.pop(-1), end=' ')
    print()
    print("After")
    print_list(st)

def problem_6():
    print("### The result of problem 6 ###")
    st = [1, 2]
    print("Before")
    print_list(st)
    st[2:] = [3, 4, 5]
    print("After")
    print_list(st)

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
