A1 = [0, 1, 2, 3, 6, 10, 11, 17]    #declares set1
B2 = [1, 2, 3, 4, 6, 11, 17]        #declares set2
C3 = [0, 1, 2, 3, 4, 5, 6, 7, 8]    #declares set3


def finding_nemo(array, start, end): #declares the operation of the array
    if (start > end):                               #1st condition
        return end + 1                              #returns the output of the statement when condition is satisfied

    if (start != array[start]):                     #2nd condition
        return start;                               #returns the output of the statement when condition is satisfied

    mid = int((start + end) / 2)                    #declaration of a variable

    if (array[mid] == mid):                         #3rd condition in line with the declaration
        return finding_nemo(array, mid + 1, end)    #returns the output of the statement when condition is satisfied

    return finding_nemo(array, start, mid)          #if no condition is satisfied return the given statement

A = len(A1)
print("Smallest missing in first set is", finding_nemo(A1, 0, A - 1))

B = len(B2)
print("Smallest missing in second set is", finding_nemo(B2, 0, B - 1))

C = len(C3)
print("Smallest missing in third set is", finding_nemo(C3, 0, C - 1))