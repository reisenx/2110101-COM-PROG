#include<iostream>
#include<vector>
using namespace std;

int N, M;
bool is_game_end = false;
char PLAYER[2] = {'1', '2'};
int DIRECTIONS[8][2] = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}, {-1, 1}, {1, -1}, {-1, -1}, {1, 1}};
vector<int> column_sequence, column_pieces;
vector<vector<char>> board;

// Get row index of a piece
int get_row(const int &col)
{
    return M - (column_pieces[col] + 1);
}

// Check if the (row, col) is inside the board
bool is_inside_board(const int &row, const int &col)
{
    return (row >= 0) && (row < M) && (col >= 0) && (col < N);
}

// Check if a piece in (row, col) belongs to a player
bool is_player_piece(const int &row, const int &col, const char &player)
{
    return is_inside_board(row, col) && board[row][col] == player;
}

// Display board
void display_board()
{
    for(vector<char> &row : board)
    {
        for(char &c : row) { cout << c; }
        cout << '\n';
    }
}

// A player drop a piece into a board
bool drop_piece(const int &row, const int &col, const char &player)
{
    if(is_inside_board(row, col))
    {
        board[row][col] = player;
        ++column_pieces[col];
        return true;
    }
    return false;
}

// Check if the player wins a game
// DIRECTIONS
// - East      (0, 1)   | West      (0, -1)
// - North     (-1, 0)  | South     (1, 0)
// - Northeast (-1, 1)  | Southwest (1, -1)
// - Northwest (-1, -1) | Southeast (1, 1)
bool is_player_win(const int &row, const int &col, const char &player)
{
    // Count 4 consecutive pieces in each direction
    int count = 1;
    for(int i = 0; i < 8; i++)
    {
        // Reset when count on a new direction
        if(i % 2 == 0) { count = 1; }
        // Counting
        int dr = DIRECTIONS[i][0];
        int dc = DIRECTIONS[i][1];
        for(int x = 1; x <= 3; x++)
        {
            if(!is_player_piece(row + (dr * x), col + (dc * x), player)) { break; }
            ++count;
        }
        // The player has 4 consecutive pieces
        if(count >= 4) { return true; }
    }
    return false;
}

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input and construct board
    cin >> N >> M;
    int temp;
    while(cin >> temp)
    {
        column_sequence.push_back(temp - 1);
    }
    board.assign(M, vector<char>(N, '.'));
    column_pieces.assign(N, 0);

    // Play a game
    for(int turn = 0; turn < column_sequence.size(); turn++)
    {
        // Get player information
        int col = column_sequence[turn];
        int row = get_row(col);
        char player = PLAYER[turn % 2];
        // Drop a piece
        bool is_column_full = !(drop_piece(row, col, player));

        // Check if the player wins
        if(turn >= 3 && is_player_win(row, col, player))
        {
            cout << "Player " << player << " wins\n";
            is_game_end = true;
            break;
        }
        // Check if the column is full
        if(turn >= M - 1 && is_column_full)
        {
            cout << "Column full\n";
            is_game_end = true;
            break;
        }
        // Check if the board is full
        if(turn == (M * N) - 1)
        {
            cout << "Board full\n";
            is_game_end = true;
            break;
        }
    }
    // No one wins after all turns
    if(!is_game_end) { cout << "No more moves\n"; }
    display_board();
    return 0;
}