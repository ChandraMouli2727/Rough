
s = []
s.append('https://www.cnn.com/')
s.append('https://www.cnn.com/world')
s.append('https://www.cnn.com/india')
s.append('https://www.cnn.com/china')

print(s)
s.pop()
print(s)
print(s[-1]) #lifo

from collections import deque
stack = deque()

print(dir(stack))

stack.append("https://www.cnn.com/")
print(stack)

stack.append("https://www.cnn.com/world")
print(stack)

stack.append("https://www.cnn.com/india")
stack.append("https://www.cnn.com/china")
print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())



class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)




s = Stack()
s.push(5)

print(s)
a = s.is_empty()
print(a)

s.push(9)
s.push(34)
s.push(78)
s.push(12)

print(s.peek())

#reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
#Write a function in python that can reverse a string using stack data structure
def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ''
    while stack.size()!=0:
        rstr += stack.pop()

    return rstr


if __name__ == '__main__':
    print(reverse_string("We will conquere COVI-19"))
    print(reverse_string("I am the king"))

'''
Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]".
'''

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0


if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
