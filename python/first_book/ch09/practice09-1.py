def to_list(t):
    ret = []
    for i in t:
        ret.append(i)
    return ret

def problem_1():
    print("### The result of problem 1 ###")
    ds = (1, 2, 3)
    ds = to_list(ds)
    print(ds)

    ds = "hello"
    ds = to_list(ds)
    print(ds)

def main():
    problem_1()
    print("-----------------------------")

main()
