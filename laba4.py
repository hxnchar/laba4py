n = int(input("Input n..."))
m = int(input("Input m..."))
result = 0
if n>=pow(10, m-1):
    for m in range(m, 0, -1):
        result += n % 10
        n /= 10
    print(f"Result is {int(result)}.")
else:
    print("M is greater than the number of digits of n")
k = input()