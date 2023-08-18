
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        t_count = 0
        l = 0
        res = 0
        for r in range(len(answerKey)):
            if answerKey[r] == 'T':
                t_count += 1
            while t_count > k:
                if answerKey[l] == 'T':
                    t_count -= 1
                l += 1
            res = max(r-l+1, res)
        t_count = 0
        l = 0
        for r in range(len(answerKey)):
            if answerKey[r] == 'F':
                t_count += 1
            while t_count > k:
                if answerKey[l] == 'F':
                    t_count -= 1
                l += 1
            res = max(r-l+1, res)

        return res





