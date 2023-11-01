lst = [34, 2, 4, 6, 4, 23, 11, 34, 12, 44, 45]
data = int(input('Enter a number you want to search: '))
l = 0
r = len(lst) - 1

while l <= r:
    mid = (l + r) // 2  # Calculate the midpoint within the loop
    if data == lst[mid]:
        print(f'Number {data} found at index {mid}')
        break
    elif data > lst[mid]:
        l = mid + 1
    else:
        r = mid - 1
else:
    print('Data is not found')

        