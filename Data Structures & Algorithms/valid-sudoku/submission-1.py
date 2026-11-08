class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # r,c pass (1-3) covers squares (A,B,C) (A,D,G) -> (A, B, C, D, G)

        # r,c pass (4,5,6) covers squares (D,E,F) (B, E, H) -> (D, E, F, B, H)

        # r,c pass (7,8,9) covers squares (G, H, I) (C, F, I) -> (G, H, I , C, F)
        
        # A: 1 <-
        # B: 2
        # C: 2
        # D: 2
        # E: 1 <-
        # F: 2
        # G: 2
        # H: 2
        # I: 1 <-

        row_check = True
        for row in board:
            seen = {}
            for item in row:

                if item.isdigit():

                    seen[item] = seen.get(item, 0) + 1 
                    if seen[item] > 1:
                        row_check = False
                        break 

        column_check = True 

        for col_idx in range(9):

            column = [row[col_idx] for row in board]
            seen2 = {}
            for item in column:

                if item.isdigit():

                    seen2[item] = seen2.get(item, 0) + 1

                    if seen2[item] > 1:
                        column_check = False
                        break

        

        '''
        row_range = range(0,3) #after 3 checks turns into range(3,6)...another 3 checks into range(6,9)
        col_range = range(0,3) #changes after each check (range(3,6), range(6,9))
        # it must reset to range(0,3) after 3 checks 
'''
        box_check = True 
        for box_row in range(0,9,3):

            for box_col in range(0,9,3):

                row_range = range(box_row, box_row + 3)
                col_range = range(box_col, box_col + 3) 

                seen3 = {}

                for r in row_range:

                    for c in col_range:

                        item = board[r][c]
                        if item.isdigit():
                            
                            seen3[item] = seen3.get(item, 0) + 1
                            
                            if seen3[item] > 1:

                                box_check = False
                                break

        return row_check and column_check and box_check












            
        

        
            

            








    