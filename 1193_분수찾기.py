# 1/1
# 1/2 2/1
# 3/1 2/2 1/3
# 1/4 2/3 3/2 4/1
# 5/1 4/2 3/3 2/4 1/5
# ...

# 1
# 2~3
# 4~6
# 7~10
# s = 0+1+2+...+n-1 + 1
# e = 0+1+2+...+n-1 + n

X = int(input())
n = e = 0
while True:
    e += n
    if X <= e: break
    n += 1
# 그룹 n에 속함
s = e - (n-1)
i = X - s   # X는 그룹 n의 i번째 수 (i=0,1,2,...)
if n % 2:
    print(f'{n-i}/{i+1}')
else:
    print(f'{i+1}/{n-i}')