class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # merge the two arrays in increasing order 
        # arrays --> two pointers with the two arrays

        nums1copy = list(nums1)
        m_p, n_p = 0, 0
        ptr = 0

        while (m_p < m and n_p < n):
            if nums1copy[m_p] < nums2[n_p]:
                nums1[ptr] = nums1copy[m_p]
                m_p += 1
            else:
                nums1[ptr] = nums2[n_p]
                n_p +=1 
            ptr += 1
        if n_p != n: 
            # add rest of elements
            while (n_p < n):
                nums1[ptr] = nums2[n_p]
                n_p +=1 
                ptr += 1
        if m_p != m:
            while (m_p < m):
                nums1[ptr] = nums1copy[m_p]
                m_p += 1
                ptr += 1





        