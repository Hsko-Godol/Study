def print_list(data):
    print("list = ", end='')
    for i in range(len(data)):
        print(data[i], end=' ')
    print()

def sum_all(data):
    sum = 0
    for i in range(len(data)):
        sum += data[i]
    return sum

def show_reverse(data):
    for i in range(1, len(data)+1):
        print(data[-i], end=' ')
    print()

def problem_1():
    print("### The result of problem 1 ###")
    l = [1, 2, 3, 4, 5]
    sum = sum_all(l)
    print(sum)

def problem_2():
    print("### The result of problem 2 ###")
    l = [1, 2, 3, 4, 5]
    s = "ABCDEFG"
    show_reverse(l)
    show_reverse(s)

def main():
    problem_1()
    print("-----------------------------")

    problem_2()
    print("-----------------------------")

main()
