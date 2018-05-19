import numpy
from timeit import default_timer as timer

# Range and size of random array
RANGE = (0, 10000)
SIZE = 3000

random_array = numpy.random.randint(*RANGE, SIZE)


def sort_wrapper(sorting_method: staticmethod, array: numpy.ndarray):
    array_copy = numpy.copy(array)
    start_time = timer()

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
