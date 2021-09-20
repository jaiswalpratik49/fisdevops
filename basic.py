a = input()
b = input()

try:
    c = int(a)/int(b)
    print(c)
except (ZeroDivisionError, ValueError):
    print("B cannot be a zero or an alphabet")
else:
    print("Try block ran ")
finally:
    print("It runs no matter what")
