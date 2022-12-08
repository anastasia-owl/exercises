k = int(input())
str_num = []
for i in range(0, 4):
    str_num.append(input())

# Сортируем только числа
lst_num = []
for i in range(0, 4):
    for j in str_num[i]:
        if j != '.':
            lst_num.append(int(j))

# Определяем список уникальных значений
unique_num = list(set(lst_num))
points = 0
for item in unique_num:
    if lst_num.count(item) <= 2*k:
        points += 1

print(points)
