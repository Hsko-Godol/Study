def problem_1():
	sum = 0

	for i in [1, 3, 5, 7, 9]:
		sum = sum + i

	print("The result of problem 1 :", sum)

def problem_2():
	result = 1

	for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
		result = result * i

	print("The result of problem 2 :", result)

def problem_3():
	print("The result of problem 3 is below")
	for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
		print("7 x", i, "=", 7*i)

def problem_4():
	print("The result of problem 4 is below")
	for i in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
		print("7 x", i, "=", 7*i)

def main():
	problem_1()
	print("------------------")

	problem_2()
	print("------------------")

	problem_3()
	print("------------------")

	problem_4()
	print("------------------")

main()
