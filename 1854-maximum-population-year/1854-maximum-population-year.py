class Solution:
    def maximumPopulation(self, logs):
        events = []

        for birth, death in logs:
            events.append((birth, 1))
            events.append((death, -1))

        events.sort()

        pop = 0
        max_pop = 0
        year = 0

        for y, change in events:
            pop += change
            if pop > max_pop:
                max_pop = pop
                year = y

        return year