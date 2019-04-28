def print_list(data):
    print("list = ", end='')
    for i in range(len(data)):
        print(data[i], end=' ')
    print()

def birth_only(str):
    return str.split('-')[0]

def problem_1():
    print("### The result of problem 1 ###")
    str = "The Espresso Spirit"
    print("Lower = " + str.lower())
    print("Upper = " + str.upper())
    print("Ori = " + str)

def problem_2():
    print("### The result of problem 2 ###")
    p1 = "070609-2011xxx"
    p2 = "090716-1012xxx"
    print("Before")
    print(p1)
    print(p2)
    print("After")
    print(birth_only(p1))
    print(birth_only(p2))

def main():
    problem_1()
    print("-----------------------------")

    problem_2()
    print("-----------------------------")

main()
