class Solution:
    def findall(self,p, s):
        i = s.find(p)
        while i != -1:
            yield i
            i = s.find(p, i+1)

    def isMatch(self, s: str, p: str) -> bool:
        cursors =[] 
        is_prev_asterics = False
        cursors.append(0) #always starting from 0 but further can be several strings which matching with template
        for dummy_char in p:
             #if we meet * then next after him we looking all substtring 
            if len(cursors) < 1 : return False
            if dummy_char == '.':
                for i in range(len(cursors)):
                    cursors[i] +=1 
                is_prev_asterics = False
            elif dummy_char == '*':
                is_prev_asterics = True
            else: #regular symbol 
                if is_prev_asterics:
                    min_indx = min(cursors)
                    cursors= []
                    for n in self.findall(dummy_char,s ):
                        if n > min_indx:
                            cursors.append(n+1)
                else: 
                # search next

                    for i, val in enumerate(cursors):
                        if s[val:val+1] == dummy_char:
                            cursors[i] +=1
                        else:
                            del cursors[i]
                is_prev_asterics = False

            prev_dummy_char = dummy_char
        if prev_dummy_char == '*' and len(cursors)>0 : return True
        elif max(cursors) == len(s): return True
        else: return False

    def isMatch2(self,s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # Initialize the DP table
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # Both s and p are empty
        
        # Initialize first row (s is empty)
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]  # '*' matches zero occurrence of the preceding element
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]  # '*' matches zero occurrence
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        
        return dp[m][n]
x = Solution()
print(x.isMatch2('aab','c*a*b'))