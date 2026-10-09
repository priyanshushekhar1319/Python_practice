# N = int(input())

# num = 1
# while num * num <= N:
#     print(num * num)
#     num += 1
# Q4) Given a integer N as input print its digit
N=int(input())
while N>0:
    print(N%10,end=" ")
    N=N//10