class Friend:
    def __init__(self, name, phone_num):
        self.name = name
        self.phone_num = phone_num

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone_num

    def set_phone(self, new_phone_num):
        self.phone_num = new_phone_num

    def show_info(self):
        print('이름:', self.name)
        print('전화번호:', self.phone_num)

list_friend = list

def problem_1():
    print("### The result of problem 1 ###")
    print(type(Friend))

def problem_2():
    print("### The result of problem 2 ###")
    global list_friend
    list_friend = [Friend('윤지민', '010-111-222'),
                   Friend('이선준', '010-333-444'),
                   Friend('장지우', '010-555-666'),
                   Friend('윤지율', '010-777-888')]
    for i in list_friend:
        i.show_info()

def problem_3():
    print("### The result of problem 3 ###")
    global list_friend
    for i in list_friend:
        if i.get_name().startswith('윤'):
            i.show_info()

def problem_4():
    print("### The result of problem 3 ###")
    global list_friend
    for i in list_friend:
        if i.get_name() == '장지우':
            i.set_phone('010-999-999')
    for i in list_friend:
        i.show_info()

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
