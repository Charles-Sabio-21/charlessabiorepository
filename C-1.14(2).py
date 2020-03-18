def computed_product(nums):
    for n in range(len(nums)):
        for m in range(len(nums)):
            if n != m:
                product = nums[n] * nums[m]
                if product & 1:
                    return True
                    return False


integers = [2,4,6,8]
sequence = [1,6,4,7,8]
print(integers, computed_product(integers));
print(sequence, computed_product(sequence));