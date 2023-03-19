# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
#  если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

length_slices = int(input("Введите количество долек шоколадки в длину: "))
width_slices = int(input("Введите количество долек шоколадки в ширину: "))
number_break = int(input(" Сколько раз нужно разломить шоколадку?: "))
 
if number_break < length_slices * width_slices & number_break % length_slices == 0 or number_break % width_slices == 0:
    print(f"шоколадку с размером {length_slices}*{width_slices} долек можно разделить на {number_break} части.")
else:
    print("Увы, не вышло, не фортануло!")