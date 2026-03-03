class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonous_stack = []
        index_stack = []
        result = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while monotonous_stack and temperature > monotonous_stack[-1]:
                monotonous_stack.pop()
                index = index_stack.pop()
                result[index] = i - index
            monotonous_stack.append(temperature)
            index_stack.append(i)
        return result