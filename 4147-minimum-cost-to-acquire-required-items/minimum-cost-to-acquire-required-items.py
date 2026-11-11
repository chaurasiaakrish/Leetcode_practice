class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        case1=cost1*need1+cost2*need2
        case2=costBoth*max(need1,need2)
        case3=costBoth*min(need1,need2)
        if need1>need2:
            case3=case3+cost1*(need1-need2)
        else:
            case3=case3+cost2*(need2-need1)
        return min(case1,case2,case3)