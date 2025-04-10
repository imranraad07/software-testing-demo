from typing import List

def reverse_twice(lst: List[int]) -> List[int]:
    return list(reversed(list(reversed(lst))))

def is_sorted(xs: List[int]) -> bool:
    return all(xs[i] <= xs[i+1] for i in range(len(xs) - 1))

def buggy_sort(xs: List[int]) -> List[int]:
    # A placeholder for a buggy implementation
    return xs

def remove_duplicates(xs: List[int]) -> List[int]:
    seen = set()
    result = []
    for x in xs:
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result
