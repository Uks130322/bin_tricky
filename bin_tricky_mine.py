def find_median(nums1: list[int], nums2: list[int]) -> float:
    """
    Find median of two sorted sequences. At least one of sequences should be not empty.
    :param nums1: sorted sequence of integers
    :param nums2: sorted sequence of integers
    :return: middle value if sum of sequences' lengths is odd
             average of two middle values if sum of sequences' lengths is even
    """
    if not nums1:
        return median_of_one(nums2)
    elif not nums2:
        return median_of_one(nums1)
    elif nums1[-1] <= nums2[0]:
        return one_is_more_then_other(nums1, nums2)
    elif nums2[-1] <= nums1[0]:
        return one_is_more_then_other(nums2, nums1)
    else:
        return find_median_real_way(nums1, nums2)


def one_is_more_then_other(nums1, nums2):
    ind1 = (len(nums1) + len(nums2) - 1) // 2
    ind2 = (len(nums1) + len(nums2)) // 2
    median = 0
    for ind in [ind1, ind2]:
        if ind < len(nums1):
            median += nums1[ind]
        else:
            median += nums2[ind - len(nums1)]
    return median / 2


def median_of_one(nums):
    return (nums[len(nums) // 2] + nums[(len(nums) - 1) // 2]) / 2


def find_median_real_way(nums1, nums2):
    begin1, begin2 = 0, 0
    end1 = len(nums1) - 1
    end2 = len(nums2) - 1
    while begin1 <= end1 or begin2 <= end2:
        if begin1 == end1 and begin2 == end2:
            return (nums1[begin1] + nums2[begin2]) / 2
        if begin1 == end1:
            mid1 = begin1
        else:
            mid1 = begin1 + (end1 - begin1) // 2
        if begin2 == end2:
            mid2 = begin2
        else:
            mid2 = begin2 + (end2 - begin2) // 2 + (end2 - begin2) % 2

        if nums1[mid1] == nums2[mid2]:
            return (nums1[mid1] + nums2[mid2]) / 2

        else:
            if mid2 > 0:
                if end1 == 0 and nums2[mid2 - 1] <= nums1[mid1] <= nums2[mid2]:
                    if len(nums2) % 2 == 0:
                        return float(nums1[mid1])
                    else:
                        return (nums1[mid1] + nums2[mid2 - (end2 - begin2) % 2]) / 2
                if nums2[mid2 - 1] <= nums1[begin1] <= nums1[end1] <= nums2[mid2]:
                    return median_of_one(nums1[(begin1 + (end1 - begin1 + 1) % 2):(end1 + 1)])
            if mid1 < len(nums1) - 1:
                if end2 == 0 and nums1[mid1] <= nums2[mid2] <= nums1[mid1 + 1]:
                    if len(nums1) % 2 == 0:
                        return float(nums2[mid2])
                    else:
                        return (nums1[mid1] + nums2[mid2]) / 2
                if nums1[mid1] <= nums2[begin2] <= nums2[end2] <= nums1[mid1 + 1]:
                    return median_of_one(nums2[begin2:(end2 + 1)])
            if mid1 < len(nums1) - 1 and mid2 > 0:
                if nums2[mid2 - 1] <= nums1[mid1] <= nums2[mid2] <= nums1[mid1 + 1]:
                    if (len(nums1) + len(nums2)) % 2 == 0:
                        return (nums1[mid1] + nums2[mid2]) / 2
                    elif (end1 - begin1 + 1) % 2:
                        return float(nums1[mid1])
                    else:
                        return float(nums2[mid2])
                if nums1[mid1] <= nums2[mid2 - 1] <= nums1[mid1 + 1] <= nums2[mid2]:
                    return (nums1[mid1 + 1] + nums2[mid2 - 1]) / 2

        if nums1[mid1] > nums2[mid2]:
            end1 = mid1 + mid1 % 2
            begin2 = mid2
        else:
            begin1 = mid1
            end2 = mid2 + mid2 % 2
