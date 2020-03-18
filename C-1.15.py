def list_of_numbers(list):
    if len(list) == len(set(list)):
        return True
    else:
        return False

print("Are the set of numbers DISTINCT to each other?")

print([1, 10, 100, 1000, 10000])
print(list_of_numbers([1, 10, 100, 1000, 10000]))
print([1, 10, 100, 100, 10, 1])
print(list_of_numbers([1, 10, 100, 100, 10, 1]))