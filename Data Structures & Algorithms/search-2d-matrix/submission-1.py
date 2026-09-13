# Session 1, attempt 1
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # log(m) + log(n) == log(m*n)

        # do bst on rows and then columns
            # special case then is the last row, could be in that row potentially
        
        # we want a weird bst that checks the whole row instead of matrix[mid]
        r_left, r_right = 0, len(matrix) - 1
        row = -1
        while r_left <= r_right:
            mid = (r_left + r_right) // 2
            

            if matrix[mid][0] <= target <= matrix[mid][len(matrix[0]) - 1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                r_right = mid - 1
            else:
                r_left = mid + 1
            
        print(row)
        if row > -1:
            # then do normla bst in columns
            left, right = 0, len(matrix[row])- 1
            while left <= right:
                mid = (left + right) // 2

                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

        
        return False



