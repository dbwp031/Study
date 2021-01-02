data = list(map(int,input()))

if not data:
    print(0)

ans = data[0]
for num in data[1:]:
    if ans == 0 or (num == 0 or num == 1):
        ans+=num
    else:
        ans*=num
print(ans)