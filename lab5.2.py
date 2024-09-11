#розмір масиву
n = 7
#заповнення масиву за рисунком
arr = [[1*(j > i) if i <= n//2 else 1*(j >= n - i) for j in range(n)] for i in range(n)]
print("array:")
#виведення масиву
for r in range(n):
    print(arr[r])
