class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        indexList = []

        point1 = 0
        point2 = 0
        while point1 < len1 and point2 < len2:
            if nums1[point1] < nums2[point2]:
                indexList.append(nums1[point1])
                point1 += 1
            else:
                indexList.append(nums2[point2])
                point2 += 1
        while point1 < len1:
            indexList.append(nums1[point1])
            point1 += 1
        while point2 < len2:
            indexList.append(nums2[point2])
            point2 += 1

        if (len1 + len2) % 2 != 0:
            mid = int((len1 + len2) / 2)
            return indexList[mid]
        else:
            mid = int((len1 + len2) / 2) - 1
            return (indexList[mid] + indexList[mid + 1]) / 2