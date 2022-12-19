
def brackets(numder: int, numder_left=0, numder_right=0, sepor =''):
    if numder_left != numder or numder_right != numder:
        if numder_left < numder:
            brackets(numder, numder_left + 1, numder_right, sepor + '(')
        if numder_right < numder_left:
            brackets(numder, numder_left, numder_right + 1, sepor + ')')
    else:
        print(sepor)

def main():
    numder = int(input())
    print(brackets(numder))

if __name__ == "__main__":
    main()