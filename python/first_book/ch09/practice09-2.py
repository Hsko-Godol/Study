def problem_1():
    print("### The result of problem 1 ###")
    for i in range(9, 0, -1):
        print(7 * i, end=' ')
    print()

def problem_2():
    print("### The result of problem 2 ###")
    tuple_result = tuple(range(1, 100)) + tuple(range(100, 0, -1))
    print(tuple_result)

def main():
    problem_1()
    print("-----------------------------")

    problem_2()
    print("-----------------------------")

main()
