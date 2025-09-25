import array

list_variable = [1, "daffa", 1+1j, 2.3, True]
exp_array = array.array("i",[1,2,3,4,5])        # i itu integer, dan harus sama tipenya, klau beda error 
var_arr = [1,2,3,4,5,6]
var_arr_loop = [0 for i in range(10)]

for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i+1

    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None
    
    print(f"Current element: {current_element}, next element: {next_element}")

# algoritma two pointers
var_arr2 = [2,23,1,45,100]
left_pointer = var_arr2[0]

for i in range(2,len(var_arr2)):
    right_pointer = var_arr2[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer
    print(left_pointer)

print(type(exp_array))
print(type(list_variable))
print(var_arr)
print(var_arr_loop)