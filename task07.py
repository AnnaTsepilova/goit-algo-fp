import random
import matplotlib.pyplot as plt


# Функція для симуляції кидання кубиків
def roll_dice(num_rolls):
    # Ініціалізуємо словник для підрахунку кількості випадків кожної суми
    sums_count = {i: 0 for i in range(2, 13)}

    # Симуляція кидків
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sums_count[total] += 1

    # Розрахунок ймовірностей
    probabilities = {k: v / num_rolls for k, v in sums_count.items()}

    return sums_count, probabilities


# Функція для побудови графіку ймовірностей
def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність суми при киданні двох кубиків (Метод Монте-Карло)')
    plt.show()


# Параметри симуляції
num_rolls = 100000  # Кількість кидків

# Запускаємо симуляцію
sums_count, probabilities = roll_dice(num_rolls)

# Виведення ймовірностей у таблиці
print("Сума\tКількість\tЙмовірність")
for total, count in sums_count.items():
    print(f"{total}\t{count}\t\t{probabilities[total]:.4f}")

# Побудова графіку
plot_probabilities(probabilities)
