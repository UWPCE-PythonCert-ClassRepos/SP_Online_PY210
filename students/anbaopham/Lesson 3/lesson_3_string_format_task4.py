
def task_4(seq):
    nums = []
    for i in seq:
        #n = "{:02d}".format(i)
        nums.append("{:02d}".format(i))
    newNums = nums[-2::] + nums[2:-2] + nums[0:2]
    print(newNums)

seq=(4,30, 2017, 2,27)
task_4(seq)
