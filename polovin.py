import time

def polovin_del():

    func_str = input("введите функцию: ")
    def f(x):
        return eval(func_str)

    a = float(input("левая граница отрезка a: "))
    b = float(input("првавая граница отрезка b: "))
    epsilon_input = input("введите точность: ")
    epsilon = float(epsilon_input) if epsilon_input else 1e-5

    if f(a) * f(b) > 0:
        print("у функции нте знаков на отрезке, метод не применим")
        return

    max_iterations = 100

    for i in range(max_iterations):
        c = (a + b) / 2
        f_c = f(c)

        print(f"итерация {i + 1}:")
        print(f"c = {c:<20.10f}", end=" ")
        print(f"f(c) = {f_c:<20.10f}")

        if abs(f_c) < epsilon:
            print(f"\nрешение: x = {c}")
            return

        if f(a) * f_c < 0:
            b = c
        else:
            a = c

    print("\nметод не получился за максимальное кол-во итераций")

if __name__ == "__main__":
    polovin_del()

time.sleep(60)