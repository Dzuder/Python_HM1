# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
#  а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

sum = int(input("Введите общее количество журавликов: "))
if sum % 6 == 0:
    katya = int((sum / 3) * 2)
    petya = int((katya / 2)/2)
    sergey = petya
    print(f"Сережа сделал {sergey}, Петя- {petya}, а Катья {katya} журавликов.")

else:
    print("По условиям задачи количество журавликов должно быть кратно 6")