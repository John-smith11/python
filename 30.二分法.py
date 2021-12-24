# 算法：高效解决问题的方法
# 算法之二分法

# 需求：有一个按照从小到大顺序排列的数字列表,查找列表中的某个数，怎样更高效
nums = [-3,4,100,22,15,11,7,77,89]
nums.sort()

def binary_search(find_num,l):
    print(l)
    if len(l) == 0:
        print('找的值不存在')
        return

    mid_idex = len(l) // 2

    if find_num > l[mid_idex]:
        # 若存在则在列表右半边
        l = l[mid_idex+1 : ]
        binary_search(find_num, l)
    elif find_num < l[mid_idex]:
        # 若存在则在列表左半边
        l = l[ : mid_idex]
        binary_search(find_num, l)
    else :
        print('找到了')

# binary_search(11,nums)
# binary_search(89,nums)
binary_search(108,nums)