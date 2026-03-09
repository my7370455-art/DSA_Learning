#You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

#Return the minimum number of CPU intervals required to complete all tasks.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        task_counts = Counter(tasks)
        max_count = max(task_counts.values())
        max_count_tasks = sum(1 for count in task_counts.values() if count == max_count)

        # Calculate the number of intervals needed
        intervals = (max_count - 1) * (n + 1) + max_count_tasks

        # The result is the maximum between the calculated intervals and the total number of tasks
        return max(intervals, len(tasks))