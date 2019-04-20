def int_div(x, y):
	x_int = int(x)
	y_int = int(y)

	print("몫:", x_int // y_int)
	print("나머지:", x_int % y_int)

def problem_1():
	print("### The result of problem 1 ###")
	int_div(5, 2)

def bet_sum(x, y):
	x_int = int(x)
	y_int = int(y)
	start = x_int+1
	end = y_int
	sum = 0
	
	for i in range(start, end):
		sum += i

	return sum

def problem_2():
	print("### The result of problem 2 ###")
	print(bet_sum(2, 5))
	print(bet_sum(1, 5))

def main():
	problem_1()
	print("-----------------------------")

	problem_2()
	print("-----------------------------")

main()
