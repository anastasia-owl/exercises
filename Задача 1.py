
def binary(numder: int):
    lst_binary = []
    while numder >= 1:
        lst_binary.append(numder%2)
        numder = numder // 2
    str_binary = ''
    for item in lst_binary:
        str_binary = str_binary + str(item)
    print(str_binary[::-1])

def main():
    numder = int(input())
    print(binary(numder))

if __name__ == "__main__":
    main()