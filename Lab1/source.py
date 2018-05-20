import numpy
from timeit import default_timer as timer

# Range and size of random array
RANGE = (0, 100000)
SIZE = 3000

random_array = numpy.random.randint(*RANGE, SIZE)


def sort_wrapper(sorting_method: staticmethod, array: numpy.ndarray):
    array_copy = numpy.copy(array)
    start_time = timer()

    if sorting_method is quicksort:
        sorted_array = sorting_method(array_copy, 0, len(array_copy)-1)
    else:
        sorted_array = sorting_method(array_copy)

    time_elapsed = timer() - start_time
    return sorted_array, time_elapsed


def bubble_sort(array: numpy.ndarray):
    for _ in range(len(array)):
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]

    return array


def selection_sort(array: numpy.ndarray):
    for i, _ in enumerate(array):
        min_index = numpy.argmin(array[i:]) + i
        array[i], array[min_index] = array[min_index], array[i]

    return array


def quicksort(array: numpy.ndarray, lo, hi):
    if lo < hi:
        pp = partition(array, lo, hi)
        quicksort(array, lo, pp-1)
        quicksort(array, pp + 1, hi)

    return array
       
       
def partition(array: numpy.ndarray, lo, hi):
    pivot = array[lo]
    i = lo + 1
    j = hi
    while i < j:
        while i <= j and array[i] <= pivot:
            i += 1
        while i <= j and array[j] >= pivot:
            j -= 1

        if i > j:
            break
        else:
            array[i], array[j] = array[j], array[i]

    array[lo], array[j] = array[j], array[lo]

    return j
        

for algorithm in [bubble_sort, selection_sort, quicksort]:
    print('Algorithm: {:.<30} time: {}'.format(algorithm.__name__, sort_wrapper(algorithm, random_array)[1]))
