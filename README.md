## 记录我在用python刷leetcode中各个题的解题思路
## the answers for leetcode problem by python


### 31.NextPermutation:
这个题是要求找到给定数组排列的下一个 [字典序](https://zh.wikipedia.org/zh-hans/%E5%AD%97%E5%85%B8%E5%BA%8F)，如果把给的数组当作一个组合数，则下一个字典序
就是找到在这些数所有排列组合数中略大于这个数的组合数，如果没有，就按升序返回。从左往右看时，如果是递增或不变则这个数是当前组合数中最大的，直接转置即可。如果递增不变中断了
那中断的地方则是可增加最小的地方，然后将这个数与其右边最小大于它的数交换，然后再转置这个位置的右边，即为所得字典序。

### 33.Search in Rotated Sorted Array:
用最简单粗暴的办法，直接循环比较，下一部用二分查找来优化