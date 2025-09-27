import time

def metod_gays(a, b):
    n = len(b)
    
    for i in range(n):
        max_row = max(range(i, n), key=lambda r: abs(a[r][i])) 
        a[i], a[max_row] = a[max_row], a[i]
        b[i], b[max_row] = b[max_row], b[i]
        print(f"итерация {i+1}:")
        for row in a:
            print(row, end=" ")
        print(b)
        
        for j in range(i+1, n):
            if a[i][i] != 0:
                factor = a[j][i] / a[i][i]
                for k in range(i, n):
                    a[j][k] -= factor * a[i][k]
                b[j] -= factor * b[i]
            else:
                print("нельзя на ноль делить, грустно")
                return

    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - sum(a[i][j] * x[j] for j in range(i+1, n))) / a[i][i]

    print("\nрешение: ")
    print(x)

n = int(input("количество переменных: "))

A = []
for i in range(n):
    row = list(map(float, input(f"введите {i+1}-ю строку матрицы через пробел: ").split()))
    A.append(row)
B = []
for i in range(n):
    b_value = float(input(f"введите правую часть {i+1}-го уравнения: "))
    B.append(b_value)

metod_gays(A, B)

time.sleep(60)
