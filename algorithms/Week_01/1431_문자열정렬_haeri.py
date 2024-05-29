# 데스크톱
import sys
sys.stdin=open("./Desktop/input.txt","r")
input=sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
    data.append(input().strip())

def get_sum_of_int(x):
    x = list(x)
    sum_of_int = 0
    for data in x:
        try:
            sum_of_int += int(data)
        except:
            pass
    return sum_of_int

data = sorted(data, key=lambda x:(len(x), get_sum_of_int(x), x))

for x in data:
    print(x)