class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences)
        def bin_search(mid):
            # return 1 if more than upper, 0 if correct and -1 if less than lower
            start = mid 
            for i in range(n-1,-1,-1):
                new = start - differences[i] 
                # print("new",new)
                if new > upper :
                    return  1 
                if new < lower :
                    return -1 
                start = new
            return 0 
        def find1():
            # for finding lower bound
            ans = -1 
            l,r = lower,upper
            while l <= r :
                mid = l + (r-l) // 2 
                res = bin_search(mid)
                print(res,mid)
                if res == 0 :
                    ans = mid 
                    r = mid - 1 
                if res == -1 :
                    l = mid + 1 
                if res == 1 :
                    r = mid - 1 
            return ans
        print(find1())
        def find2():
            # for finding upper bound
            ans = -1 
            l,r = lower,upper
            while l <= r :
                mid = l + (r-l) // 2 
                res = bin_search(mid)
                if res == 0 :
                    ans = mid 
                    l = mid + 1
                if res == -1 :
                    l = mid + 1 
                if res == 1 :
                    r = mid - 1 
            return ans
        print(find2())
        a,b = find1(),find2()
        if a == -1 or b == -1 :
            return 0
        print(a,b)
        return b - a + 1
        return -1 
            