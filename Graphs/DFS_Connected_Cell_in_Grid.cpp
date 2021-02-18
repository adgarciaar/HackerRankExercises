#include <bits/stdc++.h>

using namespace std;

int getNumberCellsRegion(int row, int column, int n, int m,
      vector<vector<bool>> &visitedCells, vector<vector<int>> &grid){

    if(row > n-1 || column > m-1 || row < 0 || column < 0){
        return 0;
    }else{
        if( visitedCells[row][column] == true ){
            return 0;
        }else{
            visitedCells[row][column] = true;
            if( grid[row][column] == 0 ){
                return 0;
            }else{
                int numberCellsRegion = 1;
                numberCellsRegion += getNumberCellsRegion(row+1, column, n, m,
                  visitedCells, grid);
                numberCellsRegion += getNumberCellsRegion(row, column+1, n, m,
                  visitedCells, grid);
                numberCellsRegion += getNumberCellsRegion(row-1, column, n, m,
                  visitedCells, grid);
                numberCellsRegion += getNumberCellsRegion(row, column-1, n, m,
                  visitedCells, grid);
                numberCellsRegion += getNumberCellsRegion(row+1, column+1, n, m,
                  visitedCells, grid);
                numberCellsRegion += getNumberCellsRegion(row-1, column-1, n, m,
                  visitedCells, grid);
                numberCellsRegion += getNumberCellsRegion(row+1, column-1, n, m,
                  visitedCells, grid);
                numberCellsRegion += getNumberCellsRegion(row-1, column+1, n, m,
                  visitedCells, grid);
                return numberCellsRegion;
            }
        }
    }
}

// Complete the maxRegion function below.
int maxRegion(vector<vector<int>> grid) {

    vector< pair<int, int> > filledCells;
    int n = grid.size(), m;
    int i, j;
    for (i = 0; i < grid.size(); i++) {
        for (j = 0; j < grid[i].size(); j++) {
            if( grid[i][j] == 1 ){
                pair<int, int> location;
                location.first = i;
                location.second = j;
                filledCells.push_back(location);
            }
        }
    }
    m = j;

    vector< vector<bool> > visitedCells(n);
    for (i = 0; i < n; i++) {
        visitedCells[i].resize(m);
        for (j = 0; j < m; j++) {
            visitedCells[i].push_back(false); // not visited yet
        }
    }

    int numberCellsLargestRegion = 0;
    int numberCellsNextRegion = 0;
    int row, column;
    for (i = 0; i < filledCells.size(); i++) {
        row = filledCells[i].first;
        column = filledCells[i].second;
        if( visitedCells[row][column] == false ){
            numberCellsNextRegion = getNumberCellsRegion(row, column, n, m,
                visitedCells, grid);
            if( numberCellsNextRegion > numberCellsLargestRegion ){
                numberCellsLargestRegion = numberCellsNextRegion;
            }
        }
    }
    return numberCellsLargestRegion;
}

int main()
{
    // ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int m;
    cin >> m;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<vector<int>> grid(n);
    for (int i = 0; i < n; i++) {
        grid[i].resize(m);

        for (int j = 0; j < m; j++) {
            cin >> grid[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int res = maxRegion(grid);

    // fout << res << "\n";
    cout << res << "\n";

    // fout.close();

    return 0;
}
