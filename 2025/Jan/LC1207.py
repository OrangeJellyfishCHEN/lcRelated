from collections import Counter
from typing import List
class LC1207:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_counter = Counter(arr)
        return len(arr_counter.keys()) == len(set(arr_counter.values()))