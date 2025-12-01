s1 = input()
s2 = input()
s3 = input()

temp = 0
if s1.isdecimal():
    temp = int(s1) + 3
elif s2.isdecimal():
    temp = int(s2) + 2
elif s3.isdecimal():
    temp = int(s3) + 1

if temp % 3 == 0 and temp % 5 == 0:
    print("FizzBuzz")
elif temp % 3 == 0:
    print("Fizz")
elif temp % 5 == 0:
    print("Buzz")
else:
    print(temp)