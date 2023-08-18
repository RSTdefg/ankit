
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        print(nums)
        arr = [n for n in range(len(nums))]
        m = {}
        val_to_index = {}
        for i, n in enumerate(nums):
            val_to_index[n] = i
        maxi = 0
        def union(a, b):
            if arr[a] == a:
                arr[b] = a
                return a
            arr[a] = union(arr[a], b)
            return arr[a]
        for i, n in enumerate(nums):
            if n + 1 in m and n - 1 in m:
                r = union(val_to_index[n+1], i)
                l = union(val_to_index[n-1], val_to_index[n+1])
                m[nums[l]] += m[nums[r]] + 1
                # if n == -1:
                #     print(m[nums[l]])
                m[n] = m[nums[l]]
                maxi = max(maxi, m[nums[l]])
            elif n + 1 in m:
                r = union(val_to_index[n+1], i)
                m[nums[r]] += 1
                m[n] = m[nums[r]]
                maxi = max(maxi, m[nums[r]])
            elif n - 1 in m:
                l = union(val_to_index[n-1], i)
                m[nums[l]] += 1
                m[n] = m[nums[l]]
                maxi = max(maxi, m[nums[l]])
            else:
                m[n] = 1
                maxi = max(maxi,1)
        # print(m)
        # print(sorted(nums))
        # print(arr)
        return maxi
