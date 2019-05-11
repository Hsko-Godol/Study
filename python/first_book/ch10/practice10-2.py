def add1(s):
    if type(s) is list:
        for i in range(len(s)):
            s[i] += 1

def problem_1():
    print("### The result of problem 1 ###")
    st = list(range(1, 6))
    add1(st)
    print(st)

def main():
    problem_1()
    print("-----------------------------")

main()
