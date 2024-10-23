numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
filtered_nums = [i for i in numbers if i is not None]
srznach = sum(filtered_nums)/(len(filtered_nums)+1)
for x in range(len(numbers)):
    if numbers[x] == None:
        numbers[x] = srznach



print("Измененный список:", numbers)
