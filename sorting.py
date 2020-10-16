import random


class SortStrategy:
    def __init__(self, app):
        self.app = app

    def sort(self, array):
        pass


class BubbleSort(SortStrategy):
    def sort(self, array):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(array) - 1):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swapped = True
                    self.app.loop()


class InsertionSort(SortStrategy):
    def sort(self, array):
        for i in range(len(array)):
            cursor = array[i]
            pos = i
            while pos > 0 and array[pos - 1] > cursor:
                array[pos] = array[pos - 1]
                pos = pos - 1

            array[pos] = cursor
            self.app.loop()


class SelectionSort(SortStrategy):
    def sort(self, array):
        for i in range(len(array)):
            lowest_index = i
            for j in range(i + 1, len(array)):
                if array[j] < array[lowest_index]:
                    lowest_index = j
            array[lowest_index], array[i] = array[i], array[lowest_index]
            self.app.loop()


class QuickSort(SortStrategy):
    def sort(self, array):
        self.quick_sort(array, 0, len(array) - 1)

    def quick_sort(self, array, first, last):
        if first >= last:
            return

        i, j = first, last
        pivot = array[random.randint(first, last)]

        while i <= j:
            self.app.loop()
            while array[i] < pivot:
                i += 1
            while array[j] > pivot:
                j -= 1
            if i <= j:
                array[i], array[j] = array[j], array[i]
                i, j = i + 1, j - 1
        self.quick_sort(array, first, j)
        self.quick_sort(array, i, last)


class MergeSort(SortStrategy):

    def sort(self, array):
        self.merge_sort(array, 0, len(array) - 1)

    def merge_sort(self, array, left, right):
        mid_point = (left + right) // 2
        if left < right:
            self.merge_sort(array, left, mid_point)
            self.merge_sort(array, mid_point + 1, right)
            self.merge(array, left, mid_point, mid_point + 1, right)

    def merge(self, array, x1, y1, x2, y2):
        i = x1
        j = x2
        temp = []
        while i <= y1 and j <= y2:
            if array[i] < array[j]:
                temp.append(array[i])
                i += 1
            else:
                temp.append(array[j])
                j += 1
        while i <= y1:
            temp.append(array[i])
            i += 1
        while j <= y2:
            temp.append(array[j])
            j += 1
        j = 0
        for i in range(x1, y2 + 1):
            array[i] = temp[j]
            j += 1
            self.app.loop()
