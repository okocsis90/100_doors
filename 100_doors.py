doors_actual = ["closed"] * 100

def change_status(x, y):
    if x[y] == "closed":
        x[y] = "opened"
    else:
        x[y] = "closed" 

actual_number = 0
n = 1

while n < 101:   
    for element in doors_actual:
        change_status(doors_actual, actual_number)
        if actual_number + n < 99:
            actual_number += n
        else:
            break
    actual_number = n
    n += 1

print("The following doors are open: ", end="")
for position, item in enumerate(doors_actual):
    if item == "opened":
        print(position + 1, end=", ")
    
print()