def inequality(number_1, number_2):
    if len(number_1) == len(number_2):
        return number_1 > number_2
    else:
        var1 = number_1 + number_2
        var2 = number_2 + number_1
        return var1 > var2


def largest_number(n: int, numbers: str) -> str:
    lst_numbers = [x for x in numbers.split(' ')]
    for i in range(1, len(lst_numbers)):
        inequality_num = lst_numbers[i]
        j = i
        while j > 0 and inequality(inequality_num, lst_numbers[j-1]):
            lst_numbers[j] = lst_numbers[j-1]
            j -= 1
            lst_numbers[j] = inequality_num
    return ("".join(lst_numbers))

def main():
    print(largest_number(input(), input()))

if __name__ == "__main__":
    main()

