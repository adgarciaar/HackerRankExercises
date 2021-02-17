#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

class Graph {
    public:
        int numberNodes;
        int** matrix;

        Graph(int n) {
            this->numberNodes = n;
            // initialize matrix
            this->matrix = new int*[n];
            for (int i = 0; i < n; i++){
                *(this->matrix+i) = new int[n];
            }

            for(int i = 0; i < n; ++i){
                for(int j = 0; j < n; ++j){
                    (*(*(this->matrix+i)+j)) = 0;
                }
            }
        }

        ~Graph() {
            // delete matrix from memory
            for (int j = 0; j < this->numberNodes; j++){
                delete[] *(this->matrix+j);
            }
            delete[] this->matrix;
            this->matrix = NULL;
        }

        void add_edge(int u, int v) {
            (*(*(this->matrix+u)+v)) = 6;
            (*(*(this->matrix+v)+u)) = 6;
        }

        void printGraph(){
          cout<<endl<<endl<<"   ";
          for(int i = 0; i < this->numberNodes; ++i){
              cout<<i+1<<" ";
          }
          cout<<endl;
          for(int i = 0; i < this->numberNodes; ++i){
              cout<<i+1<<"  ";
              for(int j = 0; j < this->numberNodes; ++j){
                  cout<<(*(*(this->matrix+i)+j))<<" ";
              }
              cout<<endl;
          }
        }

        vector<int> shortest_reach(int start) {
            vector<int> shortestDistances;
            bool visitedNodes[this->numberNodes];
            for(int i = 0; i < this->numberNodes; ++i){
                shortestDistances.push_back(-1);
                visitedNodes[i] = false; // not visited yet
            }
            queue<int> auxQueue;
            queue<int> partialDistances;
            auxQueue.push( start );
            partialDistances.push(0);
            int actualNode;
            int partialDistance;
            while( !auxQueue.empty() ){
                actualNode = auxQueue.front();
                partialDistance = partialDistances.front();
                auxQueue.pop();
                partialDistances.pop();
                shortestDistances[actualNode] = partialDistance;
                for(int j = 0; j < this->numberNodes; ++j){
                    if( (*(*(this->matrix+actualNode)+j)) == 6
                        && visitedNodes[j] == false ){
                        visitedNodes[j] = true;
                        auxQueue.push( j );
                        partialDistances.push( partialDistance
                            + (*(*(this->matrix+actualNode)+j)) );
                    }
                }
            }
            return shortestDistances;
        }
};

int main() {
    int queries;
    cin >> queries;

    for (int t = 0; t < queries; t++) {

		int n, m;
        cin >> n;
        // Create a graph of size n where each edge weight is 6:
        Graph graph(n);
        cin >> m;
        // read and set edges
        for (int i = 0; i < m; i++) {
            int u, v;
            cin >> u >> v;
            u--, v--;
            // add each edge to the graph
            graph.add_edge(u, v);
        }

		int startId;
        cin >> startId;
        startId--;
        // Find shortest reach from node s
        vector<int> distances = graph.shortest_reach(startId);

        // graph.printGraph();

        for (int i = 0; i < distances.size(); i++) {
            if (i != startId) {
                cout << distances[i] << " ";
            }
        }
        cout << endl;
    }

    return 0;
}
