class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result =[]
        count = Counter(nums)
        sorted_count = dict(sorted(count.items(), key = lambda item: item[1],reverse = True))
        i = 0
        for n in sorted_count.keys():
            result.append(n)
            i+=1
            if i >= k:
                break
        return result


        