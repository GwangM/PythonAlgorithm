n=int(input())
#25마다 6개 +, 125로 나눈 몫만큼+
result=(n//25)*6+(n//125)+(n%25)//5
print(result)