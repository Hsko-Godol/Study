def print_list(data):
    print("list = ", end='')
    for i in range(len(data)):
        print(data[i], end=' ')
    print()

def problem_1():
    print("### The result of problem 1 ###")
    num = int(input("정수를 입력해주세요: "))
    if num >= 0:
        print("입력한 값은 0이거나 0보다 큽니다")
    else:
        print("입력한 값은 0보다 작습니다.")

def problem_2():
    print("### The result of problem 2 ###")
    num = 3
    print(num > 1 and num < 5)

def problem_3():
    print("### The result of problem 3 ###")
    num = 12
    print(num < 3 or num > 10)

def problem_4():
    print("### The result of problem 4 ###")
    num = 4
    print(num % 2 == 0 and num % 3 != 0)

def problem_5():
    print("### The result of problem 5 ###")
    num = int(input("정수를 입력해주세요: "))
    if num < 0:
        print("입력한 값은 0보다 작습니다.")
    elif 0 <= num < 10:
        print("입력한 값은 0 이상 10 미만입니다.")
    elif 10 <= num < 20:
        print("입력한 값은 10 이상 20 미만입니다.")
    else:
        print("입력한 값은 20 이상입니다.")

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
