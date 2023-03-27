# create a hashmap with the number of times each number appears in the list
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [] # store the list of permutations to return
        perm = [] # store each individual permutation
        count = {n:0 for n in nums} # create hashmap, initialize all counts to 0
        # update hashmap to map each number to its total count
        for n in nums:
            count[n] += 1

        # create depth for search function
        def dfs():
            # base case: when we reach the end of one list, append to the list of results
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for n in count:
                if count[n] > 0: # as long as there is a value left
                    perm.append(n)
                    count[n] -= 1 # one of the numbers has been used

                    dfs()

                    count[n] += 1 # resets count (back to original)
                    perm.pop() # remove the last added value

        dfs()
        return res





