class Solution:
    # 輸入 rowIndex 返回對應的列表
    def getRow(self, rowIndex: int) -> List[int]:
        ansRow = [1]

        if rowIndex == 0:
            return ansRow
        
        prevRow = self.getRow(rowIndex - 1)
        for i in range(len(prevRow)-1):
            ansRow.append(prevRow[i] + prevRow[i+1])

        ansRow.append(1)
        return ansRow