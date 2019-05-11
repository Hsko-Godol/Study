def problem_1():
    print("### The result of problem 1 ###")
    for i in range(2, 10):
        for j in range(1, 10):
            print(i * j, end='\t')
        print()

def main():
    problem_1()
    print("-----------------------------")

main()
