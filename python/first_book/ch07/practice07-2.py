def print_list(data):
    print("list = ", end='')
    for i in range(len(data)):
        print(data[i], end=' ')
    print()

def problem_1():
    print("### The result of problem 1 ###")
    user_input = input("입력해주세요 : ")
    if user_input.isdigit():
        print(int(user_input) ** 2)
    else:
        print("정수가 아닙니다.")

def main():
    problem_1()
    print("-----------------------------")

main()
