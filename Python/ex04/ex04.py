def mergeArrays(arr1: list, arr2: list) -> list:
    output = []
    index1 = 0
    index2 = 0
    while(index1 < len(arr1) and index2 < len(arr2)):
        if(arr1[index1] < arr2[index2]):
            output.append(arr1[index1])
            index1 += 1
        else:
            output.append(arr2[index2])
            index2 += 1

    while(index1 < len(arr1)):
        output.append(arr1[index1])
        index1 += 1
    while(index2 < len(arr2)):
        output.append(arr2[index2])
        index2 += 1
    return output

# add your own tests below and run with "python3 Python/ex04/ex04.py"
# no output means your tests passed
# tests can look like this or you can print them
# assert(mergeArrays([1,2,3], [1,2,3]) == [1,1,2,2,3,3])
