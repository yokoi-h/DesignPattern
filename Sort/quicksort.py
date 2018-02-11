# a = [10, 26, 93, 17, 77, 31, 44, 55, 20]
a = [50,10,20,30,40]
work_array = []

def quicksort(array, begin, end):

    if begin >= end:
        return

    pivot = array[begin]
    left_pos = begin + 1
    right_pos = end

    while(left_pos <= right_pos):

        while(left_pos <= end):

            if array[left_pos] > pivot:
                break
            else:
                left_pos = left_pos + 1

        print("left_pos", left_pos)

        while(right_pos >= left_pos):

            if array[right_pos] < pivot:
                break
            else:
                right_pos = right_pos - 1

        print("right_pos", right_pos)

        if left_pos < right_pos:
            print("swap")
            print("before", array)
            temp = array[left_pos]
            array[left_pos] = array[right_pos]
            array[right_pos] = temp
            print("after", array)
            left_pos = left_pos + 1
            right_pos = right_pos - 1

    print("pivot swap before", array)
    temp = array[right_pos]
    array[right_pos] = array[begin]
    array[begin] = temp
    print("pivot swap after", array)

    print("first", left_pos, end)
    quicksort(array, left_pos, end)

    print("second", begin, right_pos - 1)
    quicksort(array, begin, right_pos - 1)

quicksort(a, 0, len(a) - 1)


