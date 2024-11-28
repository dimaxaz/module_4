from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Вызов функций с первым аргументом, отличным от 0, и вторым аргументом, равным 0
result_fake = fake_divide(10, 0)
result_true = true_divide(10, 0)

# Вывод результатов на экран
print(f"Результат вызова fake_divide(10, 0): {result_fake}")
print(f"Результат вызова true_divide(10, 0): {result_true}")

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)