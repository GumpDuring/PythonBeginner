class Solution:
    def maxProfit(self, prices):
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit

# 其实非常简单，我最初的想法没问题，遍历，动态存取最大值或最小值。但是没想清楚细节。
# 最初：记录最大值与最小值，通过遍历实现。
# 实际：只寻找最小值即可，记录最低价，最大利润（通过当前价格与记录的最低价相减），一次遍历即可找出。
# 将最低价初始值写成无限大，可以使得遍历第一元素时保证无法卖出（maxprofit=0）符合逻辑。
#设计成price-minprice可以解决买入后全部低价无法获利时返回0的要求。
#我错在了记录最低价和最高价，本身用前面的低价和后面的高价确实可以算出最大利润，但是引入了新问题：
# 记录两个值需要两个指针，如何保证最大值在最小值后面？无法解决，徒增难度。用题解算法一次遍历就可以保证方向性。