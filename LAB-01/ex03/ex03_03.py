def tao_tuple_tu_list(lst):
    return tuple(lst)

input_list = input("nhap danh sach cac so, cach nha bang dau phay: ")
numbers = list(map(int, input_list.split(',')))

my_tuple = tao_tuple_tu_list(numbers)
print("List: ",numbers)
print("Tuple tao tu list:", my_tuple)