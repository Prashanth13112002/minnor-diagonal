class solution:
    def minor_diagonal(selfself,arr):
        n=len(arr)-1
        sum=0
        for i in range (n+1):
            sum+=(arr[i][n])
            n-=1
        return sum
a1=solution()
row =int(input())
arr=[]
for i in range (row):
    col=list(map(int,input().split()))
    arr.append(col)
print(a1.minor_diagonal(arr))
