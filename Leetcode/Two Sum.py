class Solution:
    def quicksort(self, matrix):
        if len(matrix) <= 1:
            return matrix
        pivot = matrix[len(matrix) // 2][0]
        left = []
        middle = []
        right = []
        for x in matrix:
            if x[0] > pivot:
                right.append(x)
            elif x[0] < pivot:
                left.append(x)
            else:
                middle.append(x)
                
        return self.quicksort(left) + middle + self.quicksort(right)
    
    def binary_search(self, matrix, e, target):
        matrix.pop(e)
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] == target:
                return matrix[mid][1]
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numsT = []
        for e, x in enumerate(nums):
            numsT.append([x, e])
        
        numsT = self.quicksort(numsT)

        for e, num in enumerate(numsT):
            nIdx = self.binary_search(list(numsT), e, (target - num[0]))
            if(nIdx != -1):
                return [num[1], nIdx]



main = Solution()
print(main.twoSum(nums=[-10,-1,-18,-19], target=-19))