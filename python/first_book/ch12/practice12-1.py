dc = {'새우깡': 700,
      '콘치즈': 850,
      '꼬깔콘': 750}

def problem_1():
    print("### The result of problem 1 ###")
    print("Before", dc, sep='\n')
    dc['홈런볼'] = 900
    print('After', dc, sep='\n')

def problem_2():
    print("### The result of problem 2 ###")
    print('Before', dc, sep='\n')
    for i in dc:
        dc[i] += 100
    print('After', dc, sep='\n')

def problem_3():
    print("### The result of problem 3 ###")
    print('Before', dc, sep='\n')
    price = dc['콘치즈']
    del dc['콘치즈']
    dc['치즈콘'] = price
    print('After', dc, sep='\n')

def main():
    problem_1()
    print("-----------------------------")

    problem_2()
    print("-----------------------------")

    problem_3()
    print("-----------------------------")

main()
