class Solution:
    def longestPalindrome(self, s: str) -> str:
        # loop by string
        end_indx = 0
        pali, dummy_str  = '','' 
        s_len = len(s)
        dummy_len = 0
        for begin_index ,symbol in enumerate(s):
            dummy_len = s_len
            while True:
            # looking for the same symbol further in next substr starting from the end

                end_indx = s[0:dummy_len].rfind(symbol)
                #print('search sub', s[begin_index:dummy_len])
                if end_indx == -1 or end_indx <  begin_index:
                    break
                dummy_str = s[begin_index:end_indx+1]
                #print(dummy_str)            
                if dummy_str== dummy_str[::-1] and len(pali)< len(dummy_str):
                    pali=dummy_str
                    break
                else:
                    dummy_len = end_indx
        # if there is no match then it's not pali
        # if we found match then check it at pali 
        # if not move further and try find next
        return (pali)

x= Solution()
print (x.longestPalindrome('abcd'))