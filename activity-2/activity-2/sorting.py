import sys


def insertion_sort(lst):
    """
    Sorts the list lst in place using insertion_sort.
    """
    pass

def merge(lst, p, q, r):
    """
    Merges two sorted partitions of lst.  This is
    performed in-place. It is assumed that the
    two partitions are contiguous in the list.

    Args:
        lst: list that is being sorted
        p: starting index of first partition
        q: ending index of first partition
        r: ending index of second partition
    """
    n1 = q - p + 1
    n2 = r - q
    left = lst[p:p+n1]
    right = lst[q+1:q+1+n2]
    left.append(float('inf'))
    right.append(float('inf'))
    i = j = 0
    for k in range(p, r+1):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1

def merge_sort(lst, p, r):
    """
    Sorts the list lst in place using merge_sort.

    Args:
        lst: list to be sorted
        p: starting index of the list, i.e 0
        r: ending index of the list, i.e. len(lst) - 1
    """
    if p < r:
        q = (p + r) // 2
        merge_sort(lst, p, q)
        merge_sort(lst, q+1, r)
        merge(lst, p, q, r)