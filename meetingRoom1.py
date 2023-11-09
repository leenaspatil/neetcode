from typing import List


def canAttendMeetings(intervals: List[List[int]]) -> bool:
    # sort to get meeting staring point

    intervals.sort(key=lambda interval: interval[0])

    for i in range(1, len(intervals)):
        # if start time of next meeting is less that end time of previous meeting means they are overlapping
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True


def main():
    canAttendMeetings([[1, 0, 1]])


if __name__ == '__main__':
    main()


def meet1(nums: List[List[int]]) -> bool:
    nums.sort(key=lambda num: nums[0])
    for i in range(1, len(nums)):

        if nums[i][0] <0:
            print()