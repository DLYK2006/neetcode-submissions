class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts = {}
        window = {}

        for i in range(len(s1)):
            counts[s1[i]] = 1 + counts.get(s1[i], 0)
            window[s2[i]] = 1 + window.get(s2[i], 0)

        if counts == window:
            return True

        left = 0

        for right in range(len(s1), len(s2)):
            window[s2[right]] = 1 + window.get(s2[right], 0)

            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                del window[s2[left]]

            left += 1

            if counts == window:
                return True

        return False