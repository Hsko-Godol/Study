def problem_1():
	print("### The result of problem 1 ###")
	for i in range(5):
		print("안녕하세요.")

def problem_2():
	print("### The result of problem 2 ###")
	for i in range(1, 10):
		print("7 x", i, "=", 7 * i)

def exp(x, y):
	result = 1
	for i in range(y):
		result = result * x
	return result

def problem_3():
	print("### The result of problem 3 ###")
	print("Result :" , exp(2, 3))

def greet():
	cnt = eval(input("인사를 몇 번 할까요? "))
	for i in range(cnt):
		print("반갑습니다.")

def problem_4():
	print("### The result of problem 4 ###")
	greet()

def main():
	problem_1()
	print("-----------------------------")

	problem_2()
	print("-----------------------------")

	problem_3()
	print("-----------------------------")

	problem_4()
	print("-----------------------------")

main()
