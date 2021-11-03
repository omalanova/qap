while True:
    try:
        s = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
        break
    except ValueError:
        print('Введено неверное значение')
        
while True:
    try:
        number = int(input("Введите число: "))
        break
    except ValueError:
        print('Введено неверное значение')

def sorted_list(list):
    sorted_list = sorted(list)
    return sorted_list

def binary_search(array, element, left, right):
    if left > right:
        return false
    middle = len(array) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
         return binary_search(array, element, left, middle-1)
    else:
        return binary_search(array, element, middle+1, right)
    
array = [i for i in range(len(s))]
array = sorted_list(s)
left = array[0]
right = array[len(s) - 1]
              
print(binary_search(array, number, left, right))
