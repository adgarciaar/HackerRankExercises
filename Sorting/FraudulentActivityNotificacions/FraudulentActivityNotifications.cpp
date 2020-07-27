#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

double findMedian(vector<int>& arrayCount, int d){

    if( d%2 != 0){ //odd

        int positionMedian = (int)d/2 + 1;

        int tempCount = 0;
        int index = -1;
        //keep while the position of median is reached
        while( tempCount < positionMedian ){
            index += 1;
            tempCount += arrayCount[index];
            //print('index:'+str(index)+' tempCount:'+str(tempCount)+' countMedian:'+str(positionMedian) )
        }
        return index;

    }else{ //even

        int positionMedian1 = d/2;
        int positionMedian2 = d/2+1;

        int median1 = 0;
        int median2 = 0;

        int tempCount = 0;
        int index = -1;
        while( tempCount < positionMedian1 ){
            index += 1;
            tempCount += arrayCount[index];
        }

        //if the two elements in the middle are the same
        if( tempCount > positionMedian1 ){
            return index;
        }else{ //keep until the next element
            int index2 = index;
            while( tempCount < positionMedian2 ){
                index += 1;
                tempCount += arrayCount[index];
            }
            //cast to double to return double, if not, it returns int
            return (index+index2) / (double)2;
        }
    }
}

// Complete the activityNotifications function below.
int activityNotifications(vector<int> expenditure, int d) {

    int notificacions = 0;

    vector<int> arrayCount(201, 0); //201 positions, all starting with zero

    for(int i=0; i<d; i++){
        arrayCount[ expenditure[i] ] += 1;
    }

    vector<int> initialArray(d);
    double median;

    for(int i=d; i<expenditure.size(); i++){

      std::copy(expenditure.begin() + i-d, expenditure.begin() + i, initialArray.begin());
      median = findMedian(arrayCount, d);

      /*for(int j=0; j<initialArray.size(); j++){
          cout<<initialArray[j]<<",";
      }*/
      //cout<<"\n"<<"Median: "<<median<<"\n";

      if( expenditure[i] >= 2*median ){
          notificacions += 1;
      }

      arrayCount[ expenditure[i] ] += 1;
      arrayCount[ expenditure[i-d] ] -= 1;
    }

    return notificacions;
}

int main()
{
    //ofstream fout(getenv("OUTPUT_PATH"));

    string nd_temp;
    getline(cin, nd_temp);

    vector<string> nd = split_string(nd_temp);

    int n = stoi(nd[0]);

    int d = stoi(nd[1]);

    string expenditure_temp_temp;
    getline(cin, expenditure_temp_temp);

    vector<string> expenditure_temp = split_string(expenditure_temp_temp);

    vector<int> expenditure(n);

    for (int i = 0; i < n; i++) {
        int expenditure_item = stoi(expenditure_temp[i]);

        expenditure[i] = expenditure_item;
    }

    int result = activityNotifications(expenditure, d);

    cout<<result<<"\n";

    //fout << result << "\n";

    //fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
