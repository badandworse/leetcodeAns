## 记录我在用python刷leetcode中各个题的解题思路
## the answers for leetcode problem by python

### 17.Letter Combinations of a Phone Number:
这题是要找到号码对应字符串的所有组合。用字典来表示数字到字符串的组合。然后遍历数字串。使其对应的字母list与前面已有的组合进行
连接即可。

### 19.Remove Nth Node From End of List:
本题要求移除倒数第n个点，进阶解法要求只遍历一遍完成。
我采用字典，将节点编号和节点存进字典里，这样遍历一遍记得到了所有，然后移除即可。

看了答案的一遍过滤的方法是用两个指针完成，让这两个指针指向的点始终差n个，当一个到达结尾的时候，另一个就是倒数第n个，即需要移除的点。


### 31.NextPermutation:
这个题是要求找到给定数组排列的下一个 [字典序](https://zh.wikipedia.org/zh-hans/%E5%AD%97%E5%85%B8%E5%BA%8F)，如果把给的数组当作一个组合数，则下一个字典序
就是找到在这些数所有排列组合数中略大于这个数的组合数，如果没有，就按升序返回。从左往右看时，如果是递增或不变则这个数是当前组合数中最大的，直接转置即可。如果递增不变中断了
那中断的地方则是可增加最小的地方，然后将这个数与其右边最小大于它的数交换，然后再转置这个位置的右边，即为所得字典序。


### 33.Search in Rotated Sorted Array:
用最简单粗暴的办法，直接循环比较，下一部用二分查找来优化
二分查找法：先用二分查找找出旋转点，再用二分查找法查找两段，看目标是否在数组中。
二分查找法其实不用找到旋转点：可以直接做，每次比较中间和两端，target一定在这两个区间，如果存在的话。

### 34.Search for a Range:
在排好序的数组中，找到与目标值相等的索引范围,用二分查找，不过再找到目标后还要继续搜索，如果是第一次找到目标，则要继续对两侧进行搜索，如果不是第一次，则根据索引与已有结果对比决定搜索哪边。如果大于范围右侧值，则继续搜索右边。如果小于左侧值，则继续搜索左边。

### 39.Combination Sum：
给定一组不重复的正整数与一个整数，在这组数中找到所有加起来等于给定整数的组合

初看这题除了暴力没啥思路，然后看了分析发现用dfs是一种很好的办法。dfs函数应该有5个参数:给定数组，当前目标值，当前索引，当前路径，与最终结果。

dfs作用:首先检查当前目标值，小于0则返回，当前路径不满足条件，等于0则表示当前路径满足条件加入到最终结果中。大于0则从当前索引开始遍历数组，递归调用dfs，更新目标值为当前目标值减去当前索引值

### 46. Permutations：
给定一组不同的数，返回所有可能的排列组合

用DP直接解，当前结果中由n-1个数的m不同组合，现在插入一个数，对每个组合来说，这个数有n个可插入的位置，因此直接遍历插入即可。即f(n)=nf(n-1).


### 47.Permutations II:
46题的升级版，给定的数可能有重复的

用46题的方法已经没办法解决，加入多重判定，虽然通过测试，但是时间很长。需要优化。

看了discussion板块，发现判断只用加入一行代码即可，即当前加入数字与当前组合中遍历的数字如果相同的话，就结结束对当前组合的遍历即可。

### 55. Jump Game:
刚看到这题，我下意识的用动态规划来做，做出答案后，超时，加入追溯功能，即在当前点如果无法达到就标记一次，下次再到这个点就直接跳过，但是仍然超时。


没有想法后，看了solution，知道了贪心算法，思路就是,从右往左遍历，看当前点能否到达上一个goodPosition。比如最右是第一个goodPosition，第二个点如果index+nums[index]>=最右的index,显然是能到达的，所以此时lastGoodPosition=这个数的索引，如果不能大于，则lastGoodPosition不变，继续向右遍历，直到遍历完起点，如果此时lastGoodPosition==0,显然应该返回True，否则返回False.


### 75.Sort Colors:
简单粗暴解法就是计数，循环一遍知道0，1，2个数即可。再循环一遍赋值。这个实名复杂度为2*O(n)

还有一种就是设定两个指针，分别指向下一个0和2应该在的地方，即乱序的最左与最右。
遇到0则交换左指针指向的数和0，然后左指针右移同时对下一个元素进行判定。遇到2则于右指针指向的数交换，右指针左移，但是继续对这个元素判定，因为换过来的数可能是0，也可能是1。遇到1不动，直到循环到达右指针指向的地方。


### 136.Single Number:
easy难度，要求线性复杂时间，直接上dict简单粗暴。

看了solution，发现了位操作这种有趣的答案。用^可以只用O(1)的空间复杂度:
0^a=a,a^a=0,a^b^a=(a^a)^b=b


### 198.House Robber
最大抢劫金额，当进行到当前房子，有两种选择，抢劫当前房子，与不抢劫当前房子。因此需要有两个变量，存抢劫当前房子的最大金额，和不抢劫当前房子的最大金额，前者等于不抢劫上一个房子的最大金额加上当前房子的金额，而后者等于不抢劫上一个房子和抢劫上一个房子中两者的较大者。

循环完毕后返回两者中的较大值即可。

时间复杂度:O(N),空间复杂度:O(1)

### 283. Move Zeroes:
初看这题，容易难度，但是根据要求限制多，如果没有这些限制，就很简单。

要满足这些条件，引入一个指针，这个指针所指向的位置的左边都是非0的，右边则全是0。从做往右遍历，遇到非0的数，将这个值赋值给当前指针指向的位置，指针位置右移。遍历完成后，将这个指针指向的右侧（包含该指针）全赋为0。

### 394.Decode String:
这题直接用栈来解，类似与初学数据结果的时候来计算一个运算式的方法。

用3个栈分别记录遇到的数字，左括号和字符。遇到数字(str.isdigt()判断)，即为即将进栈的数字，这里要判断下，如果数字栈中元素个数大于左括号栈，即这里遇到的是多位数的数字，将数字栈的栈顶项*10+当前数字。遇到左括号，进左括号栈，当前数字栈栈顶项构造完毕，开始字符串的进栈。遇到右括号，数字栈和字符串出栈，得到的数据相乘，然后左括号出栈，判断左括号是否为空。不为空，则当前结果需要加到当前字符串栈的栈顶上。如果为空，直接加到结果上。遍历玩字符串返回即可。

### 647.Palindromic Substrings:
找出给定字符串的回文子串数

首先单个字母肯定是，然后分别按1个字母或两个字母为中心往两边扩散，满足字符串就+1并继续，不满足直接跳出，检测下一个中心扩散情况。