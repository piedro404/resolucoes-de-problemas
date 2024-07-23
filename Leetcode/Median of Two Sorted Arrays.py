class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = []
            middle = []
            right = []
            for x in arr:
                if x > pivot:
                    right.append(x)
                elif x < pivot:
                    left.append(x)
                else:
                    middle.append(x)
                    
            return quicksort(left) + middle + quicksort(right)
        
        listFull = quicksort((nums1+nums2))
        if len(listFull) % 2 == 0:
            return float((listFull[(len(listFull)//2)-1] + listFull[len(listFull)//2]) / 2)
        return float(listFull[len(listFull)//2])

main = Solution()
print(main.findMedianSortedArrays([1,2],[3, 4]))