1.1
def calculate_expression(x):
    z = 1 + 1 / x**2
    f = 0.45 * z**5 + 1 / z
    return f

def main():
    # Зчитування даних з файлу input.txt
    with open('input.txt', 'r') as file:
        x = float(file.readline().strip())

    # Обчислення значення виразу
    result = calculate_expression(x)

    # Виведення результату на екран
    print(f"При x = {x}, f = {result}")

    # Запис результату у файл output.txt
    with open('output.txt', 'w') as file:
        file.write(str(result))

if __name__ == "__main__":
    main()
