import time

def proizvodnaya(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

def kasatelny():
    func_str = input("введите функцию: ")
    def f(x):
        return eval(func_str)

    x0 = float(input("начальное приближение x0: "))
    epsilon_input = input("введите точность: ")
    epsilon = float(epsilon_input) if epsilon_input else 1e-5
    max_iterations = 100

    for i in range(max_iterations):
        f_x0 = f(x0)
        df_x0 = proizvodnaya(f, x0)
        if df_x0 == 0:
            print(f"производная равняется нулю, нельзя применить метод")
            return

        x1 = x0 - f_x0 / df_x0

        print(f"итерация {i + 1}:")
        print(f"x = {x1:<20.10f}", end=" ")
        print(f"f(x) = {f_x0:<20.10f}", end=" ")
        print(f"f'(x) = {df_x0:<20.10f}")

        if abs(x1 - x0) < epsilon:
            print(f"\nрешение: x = {x1}")
            return

        x0 = x1

    print("\nметод не получился за максимальное кол-во итераций")

if __name__ == "__main__":
    kasatelny()

time.sleep(60)