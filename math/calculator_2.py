def calculate2(s: str) -> int:
    stack, cur, op = [], 0, '+'
    for c in s + '+':
        if c == " ":
            continue
        elif c.isdigit():
            cur = (cur * 10) + int(
                c)  # to get the number other than single digit ...eg if 43 then first it will be 4 next for loop ...(4 * 10) + 3 = 43

        else:
            if op == '-':
                stack.append(-cur)
                print(stack)
            elif op == '+':
                stack.append(cur)
            elif op == '*':
                stack.append(stack.pop() * cur)
            elif op == '/':
                stack.append(int(stack.pop() / cur))
            cur, op = 0, c
    return sum(stack)


def calculate1(s: str) -> int:
    """
    1. Take 3 containers:
    num -> to store current num value only
    sign -> to store sign value, initially +1
    res -> to store sum
    When ( comes these containers used for calculate sum of intergers within () brackets.
    --------------------
    2. When c is + or -
    Move num to res, because we need to empty num for next integer value.
    set num = 0
    sign = update with c
    --------------------
    3. When c is '('
    Here, we need num, res, sign to calculate sum of integers within ()
    So, move num and sign to stack => [num, sign]
    Now reset - res = 0, num = 0, sign = 1 (default)
    --------------------
    4. When c is ')' -> 2-(3+4), Here res=3, num=4, sign=1 stack [2, -]
    res +=sign*num -> calculate sum for num first, then pop items from stack, res=7
    res *=stack.pop() - > Pop sign(+ or -) to multiply with res, res = 7*(-1)
    res +=stack.pop() - > Pop integer and add with prev. sum, res = -7 + 2 - 5
    --------------------
    Simple Example: 2 - 3
    Initially res will have 2,i.e. res = 2
    then store '-' in sign. it will be used when 3 comes. ie. sign = -1
    Now 3 comes => res = res + num*sign
    Return statement: res+num*sign => res = 2 + 3(-1) = 2 - 3 = -1
    """
    num = 0
    sign = 1
    res = 0
    stack = []
    for c in s:  # iterate till last character

        if c.isdigit():  # process if there is digit
            num = num * 10 + int(c)  # for consecutive digits 98 => 9x10 + 8 = 98
        elif c in '-+':  # check for - and +
            res += num * sign
            sign = -1 if c == '-' else 1
            num = 0
        elif c == '(':
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif c == ')':
            res += sign * num
            res *= stack.pop()
            res += stack.pop()
            num = 0
    return res + (num * sign)


def main():
    n = calculate1("(1+(4+5+2)-3)+(6+8)")
    print(n)




if __name__ == '__main__':
    main()
