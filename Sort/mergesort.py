
a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
work_array = []

# def divide(array):
#
#     half = int(len(array)/2)
#     former = [val for val in array[0:half]]
#     latter = [val for val in array[half:]]
#
#     if len(former) + len(latter) <= 2:
#         work_array.append([former, latter])
#     else:
#         divide(former)
#         divide(latter)
#     return
#
# divide(a)
# print(work_array)


work_array = [[a[x]] for x in range(len(a))]
print(work_array)

def merge_array(array):

    result = []

    idx = 0
    while(idx < len(array)):
        former = array[idx]
        latter = array[idx+1] if len(array) > idx + 1 else []

        temp = former + [latter[x] for x in range(len(latter)-1, -1, -1)]

        merged = []
        while(len(temp) > 0):
            if temp[0] < temp[-1]:
                merged.append(temp[0])
                temp = temp[1:]
                print("temp upper", temp)
            else:
                merged.append(temp[-1])
                temp = temp[0:-1]
                print("temp lower", temp)

        print("merged", merged)
        result.append(merged)
        idx = idx + 2

    return result

merged = []

while(len(work_array) > 1):
    print("step")
    work_array = merge_array(work_array)

print(work_array)


def mergeSort(alist):
    print("Splitting ",alist)
    print("alist length",len(alist))
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        # i=0
        # j=0
        # k=0
        # while i < len(lefthalf) and j < len(righthalf):
        #     if lefthalf[i] < righthalf[j]:
        #         alist[k]=lefthalf[i]
        #         i=i+1
        #     else:
        #         alist[k]=righthalf[j]
        #         j=j+1
        #     k=k+1
        #
        # while i < len(lefthalf):
        #     alist[k]=lefthalf[i]
        #     i=i+1
        #     k=k+1
        #
        # while j < len(righthalf):
        #     alist[k]=righthalf[j]
        #     j=j+1
        #     k=k+1

        work_array = lefthalf + [righthalf[x] for x in range(len(righthalf)-1, -1, -1)]

        for i in range(len(alist)):
            if work_array[0] < work_array[-1]:
                alist[i] = work_array[0]
                work_array = work_array[1:]
            else:
                alist[i] = work_array[-1]
                work_array = work_array[0:-1]

    print("Merging ", alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)


