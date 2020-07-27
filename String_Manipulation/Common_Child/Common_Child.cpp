//#include <bits/stdc++.h>
#include <iostream>
#define SIZE 5001

using namespace std;

// Complete the commonChild function below.
int commonChild(string s1, string s2) {

    int a = s1.size();
    int b = s2.size();

    // //static int M[SIZE][SIZE]; //too big for the stack capacity
    // int** M = new int*[SIZE];
    // for(int i = 0; i < SIZE; ++i)
    //     M[i] = new int[SIZE];

    //rows
    int** M = new int*[SIZE];
    //columns
    for (int i = 0; i < SIZE; i++){
        *(M+i) = new int[SIZE];
    }

    // //filas
    //         this->figura = new char*[filas];
    //         //columnas
    //         for (int i = 0; i < this->filas; i++){
    //             *(this->figura+i) = new char[columnas];
    //         }

    for(int i = 0; i<=a; i++){
        for(int j = 0; j<=b; j++){
            if( i==0 || j==0 ){
                //M[i][j] = 0;
                (*(*(M+i)+j)) = 0;
            }else{
                if( s1[i-1] == s2[j-1] ){
                    //M[i][j] = M[i-1][j-1]+1;
                    (*(*(M+i)+j)) = (*(*(M+(i-1))+(j-1))) +1;
                }else{
                    //M[i][j] = max( M[i-1][j] , M[i][j-1]);
                    (*(*(M+i)+j)) = max( (*(*(M+(i-1))+j)) , (*(*(M+i)+(j-1))) );
                }
            }
        }
    }
    //cout<<"Some"<<endl;
    //int result = M[a][b]
    int result = (*(*(M+a)+b));

    //delete matrix in memory
    for (int j = 0; j < SIZE; j++){
        delete[] *(M+j);
    }
    delete[] M;

    return result;
    //return M[a][b];
}

int main()
{
    //ofstream fout(getenv("OUTPUT_PATH"));

    string s1;
    getline(cin, s1);

    string s2;
    getline(cin, s2);

    int result = commonChild(s1, s2);

    //fout << result << "\n";
    cout << result << "\n";

    //fout.close();

    return 0;
}
