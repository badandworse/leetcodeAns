#%%
#!/usr/bin/env python
#-*-coding:utf-8-*-

def heap_sort(lst):
    def sift_down(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            #类似右节点大于左节点，父节点始终和大的子节点比较与交换
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

    # 创建最大堆
    # 从第二层开始
    for start in range((len(lst) - 2) // 2, -1, -1):
        sift_down(start, len(lst) - 1)

    # 堆排序
    # 最大建立后，取出第一个节点放在最后，然后对剩余的做最大堆
    # 重复这个过程
    for end in range(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(0, end - 1)
    return lst
            
def main():
    l = [9,2,1,7,6,8,5,3,4]
    heap_sort(l)
    print(l)

if __name__ == "__main__":
    main()


3-2