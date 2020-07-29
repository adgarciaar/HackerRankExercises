#include <bits/stdc++.h>
#include <limits>

using namespace std;

// Complete the maxMin function below.
int maxMin(int k, vector<int> arr) {

    sort(arr.begin(), arr.end());
    int minimum = numeric_limits<int>::max();
    vector<int> subarr(k);

    for(int i=0; i < (arr.size()-k)+1; i++){
        std::copy(arr.begin() + i, arr.begin() + i+k, subarr.begin());
        /*for(int j=0; j < k; j++){
            cout<<subarr[j]<<'-';
        }
        cout<<'\n';*/
        if( subarr[ k-1 ] - subarr[0] < minimum ){
            minimum = subarr[ k-1 ] - subarr[0];
        }
        subarr.clear();
    }

    return minimum;

}

int main()
{
    //ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int k;
    cin >> k;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        int arr_item;
        cin >> arr_item;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        arr[i] = arr_item;
    }

    int result = maxMin(k, arr);

    cout << result << "\n";

    //fout << result << "\n";

    //fout.close();

    return 0;
}
