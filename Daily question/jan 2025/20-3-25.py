class Solution:
    def minimumCost(self, n, edges, query):
        dict1, ans, result = {}, [-1]*n, []

        def find(x):
            if x not in dict1:
                return x 
            else:
                if dict1[x] != x:
                    dict1[x] = find(dict1[x])
                return dict1[x]

        for i,j,k in edges:
            x,y = find(i),find(j)
            ans[y] = ans[y]&k

            if x != y:
                ans[y] = ans[y]&ans[x]
                dict1[x] = y

        for i,j in query:
            if i == j:
                result.append(0)
            else:
                x, y = find(i), find(j)

                if x != y:
                    result.append(-1)
                else:
                    result.append(ans[find(x)])

        return result 