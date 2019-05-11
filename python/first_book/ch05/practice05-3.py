def print_list(data, cnt):
    print("list = ", end='')
    for i in range(cnt):
        print(data[i], end=' ')
    print()

def problem_1():
    print("### The result of problem 1 ###")
    str = "Hello"
    str += "Python"
    print(str)

def main():
    problem_1()
    print("-----------------------------")

main()
