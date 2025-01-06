class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res_array = []
        rowcount =  0 
        sign = -1
        res =''
        for i in range(numRows):
            res_array.append('')

        for i in s: 
            if rowcount == numRows-1 :
                sign = sign*-1
            elif rowcount == 0 : 
                sign = sign*-1            
            
            res_array[rowcount] = res_array[rowcount]+ i
            if numRows != 1:
                rowcount = rowcount + sign
        for r in res_array:
            res= res+ r
        return res

x= Solution()
print (x.convert('123456789',5))