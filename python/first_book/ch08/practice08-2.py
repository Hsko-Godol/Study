def problem_1():
    print("### The result of problem 1 ###")
    lcm = 45
    while True:
        if lcm % 6 == 0 and lcm % 45 == 0:
            break
        lcm += 1
    print("lcm =", lcm)

def problem_2():
    print("### The result of problem 2 ###")
    gcm = 42
    while True:
        if 42 % gcm == 0 and 120 % gcm == 0:
            break
        gcm -= 1
    print("gcm =", gcm)

def main():
    problem_1()
    print("-----------------------------")

    problem_2()
    print("-----------------------------")

main()
