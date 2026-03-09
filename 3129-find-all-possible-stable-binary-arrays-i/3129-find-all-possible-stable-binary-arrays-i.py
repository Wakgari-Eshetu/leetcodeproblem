from functools import cache

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        @cache
        def count_arrays(zeros_left: int, ones_left: int, last_element: int) -> int:

            # If no zeros left
            if zeros_left == 0:
                return 1 if (last_element == 1 and ones_left <= limit) else 0

            # If no ones left
            if ones_left == 0:
                return 1 if (last_element == 0 and zeros_left <= limit) else 0

            # If last placed element was 0
            if last_element == 0:
                total = (
                    count_arrays(zeros_left - 1, ones_left, 0) +
                    count_arrays(zeros_left - 1, ones_left, 1)
                )

                if zeros_left - limit - 1 >= 0:
                    total -= count_arrays(zeros_left - limit - 1, ones_left, 1)

            # If last placed element was 1
            else:
                total = (
                    count_arrays(zeros_left, ones_left - 1, 0) +
                    count_arrays(zeros_left, ones_left - 1, 1)
                )

                if ones_left - limit - 1 >= 0:
                    total -= count_arrays(zeros_left, ones_left - limit - 1, 0)

            return total % MOD

        result = (
            count_arrays(zero, one, 0) +
            count_arrays(zero, one, 1)
        ) % MOD

        count_arrays.cache_clear()

        return result