## 记录我在用python刷leetcode中各个题的解题思路
## the answers for leetcode problem by python

### 10.Regular Expression Matching:

递归的方法:当前正则第二个字符不为'*'，很简单，比较当前，两个指针都往右移动即可，继续这样比较。如果为空，则有两种方式，第一种是正则的指针往后移动，字符串的保持不变，另一种是字符串的往后移动一位，而正则保持不变。后一种要求字符串前一位的匹配是正确的。这样递归的思想就出来了。

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

### 32.Longest Valid Parentheses:

这题首先想到的是维护一个栈，如果遇到左括号，就将当前索引进栈，如果遇到右括号就出栈，问题在于怎么更新长度。如果遇到右括号时，栈是空的，显然则是非法的，后面遇到的合法字段一定是从下一个元素开始，因此要维护一个start，如果遇到右括号时，栈不为空，栈顶元素出栈，然后再判断是否为空，如果为空，此时长度应该是出栈的index-start+1。如果不为空，长度应该为当前的index-栈顶的index，然后视情况更新最长长度。

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

### 40. Combination Sum II:
这个不能有重复的解，而数组中的数可能是重复的，所以可以先排序，然后再使用dfs,用dfs时,在同一循环中遇到重复的数时应该跳过,代码中的判断条件是i>index and nums[i]==nums[i-1]这一判定来看是否是统一层级的循环.

### 46. Permutations：
给定一组不同的数，返回所有可能的排列组合

用DP直接解，当前结果中由n-1个数的m不同组合，现在插入一个数，对每个组合来说，这个数有n个可插入的位置，因此直接遍历插入即可。即f(n)=nf(n-1).


### 47.Permutations II:
46题的升级版，给定的数可能有重复的

用46题的方法已经没办法解决，加入多重判定，虽然通过测试，但是时间很长。需要优化。

看了discussion板块，发现判断只用加入一行代码即可，即当前加入数字与当前组合中遍历的数字如果相同的话，就结结束对当前组合的遍历即可。

### 48.Rotate Image:
旋转90度的2维矩阵，必须原地修改，转置以后水平反转即可。

### 49.Group Anagrams:
普通做法,用deafultDict,每个字符串排序后是deafultDict的key。然后将原字符串加value的list中。

看了solution以后，第二种解法更好。首先他统计的是字符串中各个字符的数量。如果各个字符数量相同，那肯定组成字符串的字母是一样的。

### 55. Jump Game:
刚看到这题，我下意识的用动态规划来做，做出答案后，超时，加入追溯功能，即在当前点如果无法达到就标记一次，下次再到这个点就直接跳过，但是仍然超时。

### 56. Merge Intervals:
简单粗暴的办法会超时，可以先对list按每个元素的start的排个序，然后再遍历，看是否需要合并。这样时间复杂度是O(Nlog(N))。

没有想法后，看了solution，知道了贪心算法，思路就是,从右往左遍历，看当前点能否到达上一个goodPosition。比如最右是第一个goodPosition，第二个点如果index+nums[index]>=最右的index,显然是能到达的，所以此时lastGoodPosition=这个数的索引，如果不能大于，则lastGoodPosition不变，继续向右遍历，直到遍历完起点，如果此时lastGoodPosition==0,显然应该返回True，否则返回False.

### 62.Unique Paths:
标准的动态规划问题，不过是二维的
f(m,n)=f(m-1,n)+f(m,n-1)

### 64.Minimum Path Sum:
标准动态规划问题，f(m,n)=min(f(m-1,n)+f(m,m-1))+grid[m][n]

### 75.Sort Colors:
简单粗暴解法就是计数，循环一遍知道0，1，2个数即可。再循环一遍赋值。这个实名复杂度为2*O(n)

还有一种就是设定两个指针，分别指向下一个0和2应该在的地方，即乱序的最左与最右。
遇到0则交换左指针指向的数和0，然后左指针右移同时对下一个元素进行判定。遇到2则于右指针指向的数交换，右指针左移，但是继续对这个元素判定，因为换过来的数可能是0，也可能是1。遇到1不动，直到循环到达右指针指向的地方。

### 78.SubSets:

求一个数组的所有子集。

空集是所有集合的子集合，一个已有数组加入一个数后，它子集个数增加一倍，即原来所有子集加入这个数，构成新的。所以一个元素的数组子集有2个，两个元素的有4个，3个元素的有6个，以此类推。代码就很好写了。

### 79. Word Search：

典型的回溯法问题，唯一需要注意的是，遍历一个数组元素，只要当这个数组处于遍历的开始时才能将其封锁，标明它被访问了，再已这个字符为开始的路径被访问完后，需要将其释放，让其他路径访问到这个字符。

### 84.Largest Rectangle in Histogram:

暴力做法是O(n<sup>2</sup>)，简单直观。
在网上看到的用栈的方法：利用索引遍历数组，如果栈空或者当前高度大于栈顶高度，则让索引进栈，否则出栈，直到满足前面的条件，出栈的过程中，每出一个栈，判断栈是否为空，若为空，则遍历到的索引之前的最小高度就是刚出栈的索引对应的高度，求出这个面积去与当前记录的最大值比较决定是否更新。如果栈不为空，这当前索引-栈顶索引-1的宽度即为刚出栈的高度所能覆盖到的最大面积，求出即可。遍历完成后，如果栈不为空，需要继续出栈，每次出栈后也得判断当前栈是否为空，为空，则这个索引对应的高度就是最小高度，求对应的面积即可，否则，同样这个高度对应的宽度应该是高度数字的长度-栈顶元素索引-1，然后更新最大面积。栈空后，返回最大面积即可。

有简写代码的方式，即遍历之前往栈里压入-1，在高度最后加入0，具体不解释了。


### 94.Binary Tree Inorder Traversal:

二叉树的中序遍历，用递归是很简单的，描述里也说了。不递归的方法是类似与递归的，用到栈，如果一个元素有左子树，将其加到栈里，没有，就栈顶元素取出，放入到结果中，再遍历其右边。

### 96.Unique Binary Search Trees:

[二叉搜索树](https://zh.wikipedia.org/zh-cn/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9)的定义。动态规划的题，只是需要弄清除后面与前者的关系。i为根节点时，其左子树由[0,i-1]构成，其右子树[i-1,n]构成.查了网上资料，知道这个数列又可以成为[卡特兰数](https://zh.wikipedia.org/zh-cn/%E5%8D%A1%E5%A1%94%E5%85%B0%E6%95%B0)。

### 98.Validate Binary Search Tree:

根据bst的特性可知，bst的中序遍历应该是一个递增的数列，求出中序序列后，如果是递增的就返回True，如果不是就返回False。

### 102. Binary Tree Level Order Traversal:

每次从左到右，比z形遍历更简单。用两个栈即可。一个栈是要返回的结果，一个栈是每次遍历的点的集合。

### 105.Construct Binary Tree from Preorder and Inorder Traversal:

前序遍历的第一个数是根节点，中序遍历的根节点的左边是左子树，右边是右子树。递归即可。

### 103.Binary Tree Zigzag Level Order Traversal:

蛇形遍历,第一层从左往右，第二层从右往左依次内推，理解后挺简单的，设定一个游标，假设顶部为0层，偶数层是从左往右，奇数层从右往做，然后如何算遍历完一层呢。设定两个辅助数组，一个用来存这层的遍历结果，一个用来存放这层的节点，如果这层没有节点了，这遍历完了。每次遍历都将结果加入到最终要返回的list中。

### 114.Flatten Binary Tree to Linked List:

按前序遍历的方式扁平化二叉树，先把左子树flatten,然后找到左子树flatten后的最后一个节点，令其右子树等于根的右子树，然后令根的右子树等于根的左子树，最后令根的左子树等于None.

### 136.Single Number:
easy难度，要求线性复杂时间，直接上dict简单粗暴。

看了solution，发现了位操作这种有趣的答案。用^可以只用O(1)的空间复杂度:
0^a=a,a^a=0,a^b^a=(a^a)^b=b

### 139.Word Break:
f(n)=f(0,i) and f(i+1,n),典型的动态规划。 

### 141.Linked List Cycle:

要求不用额外的空间，没有想到，直接用列表，经过只一个节点判断它在不在列表中不在就将起加入到列表中,在就返回True,遇到空就返回False.但是超时，将列表改为字典后,通过。

不用额外空间的方法：看了solution后，发现使用两个指针，两个指针的移动速度不同，如果存在环的话，两个指针是一定会相遇的，如果不存在，快的那个会先遇到空。

### 142. Linked List Cycle II:

与141一样，如果使用额外空间很简单，用字典做就可以。

不实用额外空间就需要两个指针了,因为fast和slow 一定是在cycle上某个点相遇,现在假定起点为S，环的起点为M,fast与slow相遇的点是P, S与M的举例为H, M与P点距离为N, cycle的长度为L. 如果slow的运动举例为H+N,则fast的运动举例为2(H+N),又知fast
的举例为H+N+nl.所有H+N=nl, 所以H=nl-N.所有head和此时的slow同时开始移动,两个指针最终会在M相遇,此时,返回head即为答案。

### 144. Binary Tree Preorder Traversal:

前序遍历二叉树,非递归的方法同样要用到栈，先将根节点加入栈。然后循环出栈，将出栈的右节点压入栈，将左节点压入栈，顺序很重要。循环，直到栈空。

### 145.Binary Tree Postorder Traversal:

这题我只相当了递归版本，看了[discuss](https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45853/Accepted-Just-a-reversal-of-a-modified-Pre-order-traversal)才发现，如果我做出了
144的Preorder 即mid-left-right,那我应该可以做出mid-right-left,只要再一反转不就是left-right-mid了。突然觉得自己缺乏想象力。

### 160. Intersection of Two Linked Lists:

这题如果用hashtable来做很简单，但是这会需要O(m)或者O(n)的空间,如果想要变为O(1)的空间，需要使用两指针A和B，分别指向一个链表,然后开始像前移动，如果A移动到链表尾，立马换到另一个的链表开始，同理B也是这样。如果两个链表有交集，则一次更换后应该会同时到达第一个交点。如果存在第二次交换，则证明没有交集，应该返回空。

### 198.House Robber
最大抢劫金额，当进行到当前房子，有两种选择，抢劫当前房子，与不抢劫当前房子。因此需要有两个变量，存抢劫当前房子的最大金额，和不抢劫当前房子的最大金额，前者等于不抢劫上一个房子的最大金额加上当前房子的金额，而后者等于不抢劫上一个房子和抢劫上一个房子中两者的较大者。

循环完毕后返回两者中的较大值即可。

时间复杂度:O(N),空间复杂度:O(1)

### 206.Reverse Linked List:

非递归版本很简单，3个指针分别记录当前节点，前一个节点和下一个节点。然后变换即可。

提交的答案是递归版本,看了[答案](https://leetcode.com/problems/reverse-linked-list/solution/)才懂，我就不班门弄斧了。

### 236.Lowest Common Ancestor of a Binary Tree:

找到根节点到两个节点的路径，然后找两个路径的公共节点即可。这类似dfs,效率有点低，看了效率高的答案，用的是从root往下逐层，销量更搞。

### 283. Move Zeroes:
初看这题，容易难度，但是根据要求限制多，如果没有这些限制，就很简单。

要满足这些条件，引入一个指针，这个指针所指向的位置的左边都是非0的，右边则全是0。从做往右遍历，遇到非0的数，将这个值赋值给当前指针指向的位置，指针位置右移。遍历完成后，将这个指针指向的右侧（包含该指针）全赋为0。

### 338.Counting Bits:
只要仔细分析还是很简单的，根据一个数的二进制转换方式,f(n)=f(n/2)+n%2,实现即可。

### 394.Decode String:
这题直接用栈来解，类似与初学数据结果的时候来计算一个运算式的方法。

用3个栈分别记录遇到的数字，左括号和字符。遇到数字(str.isdigt()判断)，即为即将进栈的数字，这里要判断下，如果数字栈中元素个数大于左括号栈，即这里遇到的是多位数的数字，将数字栈的栈顶项*10+当前数字。遇到左括号，进左括号栈，当前数字栈栈顶项构造完毕，开始字符串的进栈。遇到右括号，数字栈和字符串出栈，得到的数据相乘，然后左括号出栈，判断左括号是否为空。不为空，则当前结果需要加到当前字符串栈的栈顶上。如果为空，直接加到结果上。遍历玩字符串返回即可。

### 344. Reverse String：
反转一个字符串，最直接的用python的切片，可以通过。

不用自带函数的话，设定两个指针，一个指向头，一个指向尾，同时像中间移动，每次交换两个指针指向的字符。

### 413.Arithmetic Slices:

遍历数组，得出有多少个等差数列，每个等差数列有多少个元素，n个等差数列有(n-1)(n-2)/2个子等差数列。累加即可。

动态规划思想:n(n>3)的等差数列个数为个数为3的等差数列个数和+个数为4的等差数列和+个数为5的等差数量和。dp(3)=1 dp(4)=1+dp(3) dp(5)=1+dp(4). dp(i)=dp(i-1)+1. sum(n)=dp(3)+dp(4)...

### 541. Reverse String II:
和341类似的题，加了一些限制,就按2k的间隔遍历，同时利用切片反转前k个和连接后面k个，最后连接在一起即可。

### 516. Longest Palindromic Subsequence:
动态规划问题，把字符串反转以后，这就是一个典型的[LCS问题](http://blog.csdn.net/v_JULY_v/article/details/6110269)。

### 628. Maximum Product of Three Numbers:

最大的一定是在以下两种情况中产生：最大的3个数相乘，或者两个最小的数乘以最大的数，因为负数的情况下，也有且只能有2个负数的情况下才有可能成为最大值的一部分。

### 647.Palindromic Substrings:
找出给定字符串的回文子串数

首先单个字母肯定是，然后分别按1个字母或两个字母为中心往两边扩散，满足字符串就+1并继续，不满足直接跳出，检测下一个中心扩散情况。

### 673. Number of Longest Increasing Subsequence:

这题是[Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence)小升级版，需要知道lis的数量，那就用一个n*2的数组来完成，一个用来记录当前节点lis的长度，一个用来记录当前节点lis的数量，同时记录最长的lis长度，最后遍历得到有多少个最长的lis，双循环时，如果外循环的节点值大于内循环节点值，要判断此时记录的lis与内循环的节点的lis长度比较，相等，外层的lis数要加上当前这个节点的lis数，小于，这将外层的lis长度等于当前内循环节点的lis长度，数量等于内层节点的lis数。

### 746.Min Cost Climbing Stairs：
典型的动态规划问题。
遍历cost,当前节点有两个状态，经过该阶梯的成本，与不经过该阶梯的成本。遍历完，返回两者中的最小值即可。经过的成本f(n)=min(f(n-1),f(n-2))+cost[n],不经过的成本一定是f(n-1)。
