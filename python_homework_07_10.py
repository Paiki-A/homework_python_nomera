n = int(input("Скільки чисел ви хочете ввести: "))
total_sum = 0
for i in range(n):
    num = int(input(f"Введіть число {i + 1}: "))
    total_sum += num
print("Загальна сума:", total_sum)