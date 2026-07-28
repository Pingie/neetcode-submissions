class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        bool row[10][10] = {false};
        bool col[10][10] = {false};
        bool squares[10][10] = {false};

        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                if(board[i][j] == '.') continue;

                int value = board[i][j] - '0';
                int squares_id = (i / 3) * 3 + (j/3); 

                if(row[i][value] || col[j][value] || squares[squares_id][value]) return false;

                row[i][value] = true;
                col[j][value] = true;
                squares[squares_id][value] = true;
            }
        }

        return true;
    }
};
