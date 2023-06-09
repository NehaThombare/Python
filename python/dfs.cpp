#include<iostream>
#include<list>
#include<map>
#include<queue>
using namespace std;

class Graph{
    public:

  map<int,list<int>>adjList;
  map<int,bool>visited;
  queue <int> q;

  void addEdge(int start,int dest){
    adjList[start].push_back(dest);
    adjList[dest].push_back(start);
  }

  void dfs(int a){
    visited[a]=true;
    cout<<a<<" ";
    for(int i:adjList[a]){
        if(!visited[i]){
            dfs(i);
        }
    }
  }

  void bfs(){
      if(q.empty()){
        return;
      }
      int n=q.front();
      q.pop();
      cout<<n<<" ";
      for(int i:adjList[n]){
        if(!visited[i]){
          visited[i]=true;
          q.push(i);
          }
        }
      bfs();
  } 
};

int main(){
    Graph g;
    int n,e;
    cout<<"Enter no of nodes: ";
    cin>>n;
    cout<<"Enter no of edges: ";
    cin>>e;
    int u,v;
    cout<<"Enter Edges (Start and Dest to separate press enter)"<<endl;
    for(int i=0;i<e;i++){
        cout<<"Enter edges: ";
        cin>>u;
        cin>>v;
        g.addEdge(u,v);
    }


 int x ;
 cout<<endl;
 cout<<"Enter 1 for dfs and 2 for bfs: ";
 cin>>x;
 if(x==1){
    cout<<"Path for DFS: ";
    g.dfs(0);
    cout<<endl;
 }
 else if(x==2){
    cout<<"Path for BFS: ";
    g.q.push(0);
    g.visited[0]=true;
    g.bfs();
    cout<<endl;
 }
 else
 {
    cout<<"Invalid Choice";
 }
  return 0;
}