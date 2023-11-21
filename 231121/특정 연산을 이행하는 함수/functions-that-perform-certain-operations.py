answer = ""
for n in input().split(" "):
    n = int(n)
    if n%2==0:
        answer += str(n//2)
    else:
        answer += str(n*3-20)
    answer += " "
print(answer)