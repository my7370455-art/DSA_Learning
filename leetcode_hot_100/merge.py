class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()
        merged = []
        current_interval = intervals[0]

        for next_interval in intervals[1:]:
            if next_interval[0] <= current_interval[1]:
                current_interval[1] = max(current_interval[1], next_interval[1])
            else:
                merged.append(current_interval)
                current_interval = next_interval

        merged.append(current_interval)
        return merged