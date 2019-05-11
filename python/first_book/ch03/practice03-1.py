def get_input():
    return input("첫 번째 입력: ")

def concat_and_print(input_1, input_2):
    print("두 입력의 합: " + input_1 + input_2)

def main():
    data_1 = get_input()
    data_2 = get_input()

    concat_and_print(data_1, data_2)

main()
