import re

def palindrome(string: str):
    string = re.findall('\w', string)
    numder_letter = 0
    for i in range(len(string)):
        if string[i] == string[len(string) - i - 1]:
            numder_letter += 1

    return numder_letter == len(string)

def main():
    string = input().lower()
    print(palindrome(string))

if __name__ == "__main__":
    main()