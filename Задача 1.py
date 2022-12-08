
def neighbor(lst):
    '''

    Args: список номеров домов
    Returns: список дистанций до ближайшего пустого учатка

    '''
    distance = []
    second_null = -1

    # Находим первый ноль
    i = 0
    while lst[i] != 0:
        i += 1
    first_null = i

    # Заполняем список дистанций до первого нуля
    j = 0
    while j <= first_null:
        distance.append(first_null-j)
        j += 1

    # Делаем цикл по всем 'парным' нулям
    for i in range(first_null + 1, len(lst)):
        if lst[i] == 0:
            second_null = i
        dist_null = second_null - first_null - 1
        if second_null == i:
            if dist_null % 2 == 0:
                n = dist_null/2
                j = 1
                while j <= n:
                    distance.append(j)
                    j += 1
                j = j - 1
                while j >= 0:
                    distance.append(j)
                    j = j - 1
            else:
                n = (dist_null + 1)/2
                j = 1
                while j <= n:
                    distance.append(j)
                    j += 1
                j = j - 2
                while j >= 0:
                    distance.append(j)
                    j = j - 1
            first_null = second_null

    # Заполняем список до конца от последнего нуля
    if second_null != len(lst) and second_null != -1:
        j = 1
        while j <= (len(lst) - second_null - 1):
            distance.append(j)
            j += 1

    # Если в списке участков только один ноль
    if second_null == -1:
        j = 1
        while j < (len(lst) - first_null):
            distance.append(j)
            j += 1
    return (distance)

num_str = list(map(int, input().split()))

for item in neighbor(num_str):
    print(item, end = ' ')
