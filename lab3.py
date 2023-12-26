def fibonacci(n):
    if n <= 0:
        return "Некоректне введення. Введіть ціле число більше 0."

    fib_sequence = [0, 1]

    while len(fib_sequence) <= n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence[n]

try:
    position = int(input("Введіть позицію n у послідовності Фібоначчі: "))
    result = fibonacci(position - 1)  # Оскільки ми використовуємо індексацію з 0, зменшимо позицію на 1
    print(f"Елемент на позиції {position} у послідовності Фібоначчі: {result}")
except ValueError:
    print("Некоректне введення. Будь ласка, введіть ціле число більше 0.")
