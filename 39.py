# this uses a recursive solution with a decision tree
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i,cur,total): # depth for search function, i is which candidates we can choose, cur is list of values that are in current combo, total is sum of values in cur
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # create a two-branched decision tree, one WITH the value at pos i and one without
            cur.append(candidates[i]) # append the value at i
            dfs(i,cur,total+candidates[i])
            cur.pop() # remove the value at i from cur
            dfs(i+1,cur,total) # move pointer to the next value

        dfs(0,[],0)
        return res




