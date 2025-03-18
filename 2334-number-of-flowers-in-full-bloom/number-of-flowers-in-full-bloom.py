from bisect import bisect_left,bisect_right
class Solution:
        def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
            starts = sorted(s for (s,_) in flowers)
            ends = sorted(e for (_,e) in flowers)

            import bisect

            ans = []
            for p in people:
                s_f = bisect.bisect_right(starts, p)
                e_f = bisect.bisect_left(ends, p)
                ans.append(s_f - e_f)

            return ans