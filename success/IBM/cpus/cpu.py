class Solution:
    def cpus(self, capacities: list) -> int:
        res = []
        capacities.sort()

        for capacity in capacities:
            options = [capacity, capacity - 1, capacity + 1]
            for option in options:
                if option >= 1 and option not in res:
                    res.append(option)
                    break
        res.sort()
        return len(res)


example = [1, 1, 4, 4, 1, 4]
expected = 5

test = Solution()
print(test.cpus(example))
