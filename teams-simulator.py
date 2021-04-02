import sys

## When you join a Teams meeting as a guest you are presented with
## a field to input your name. (Guest) is automatically appended
## to this name when you join. The next time you join a meeting, 
## the name field will default to the last value, which if it contains
## spaces will put double quotes around the string. The time after that,
## the quotes will need to be escaped with backslashes. Then backslashes 
## for the backslashes. Chaos ensues.

## E.g.
## input:       Ashton
## 1st meeting: Ashton (Guest)
## 2nd meeting: "Ashton (Guest)"
## 3rd meeting: "\"Ashton (Guest)\""
## 4th meeting: "\"\\\" Ashton (Guest) \\\"\""

def replace(word: str) -> str:
    result = ''

    for c in word:
        if c == '"':
            result += '\\"'
        elif c == '\\':
            result += '\\\\'
        else:
            result += c
    
    result = f'"{result}"'

    return result

def pre_proc(word: str) -> str:
    if not '(Guest)' in word:
        word += ' (Guest)'

    return word

if __name__ == '__main__':
    name = sys.argv[1]
    number = sys.argv[2]

    name = pre_proc(name)

    for i in range(int(number) - 1):
        name = replace(name)
    print(name)