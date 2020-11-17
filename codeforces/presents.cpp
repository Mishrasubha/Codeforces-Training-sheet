#include<iostream>
#include<algorithm>
#include<vector>
#define rep(i,c,n) for(int i=c;i<n;i++)
using namespace std;
int main(){
    int n,m,io;
    cin>>n;
    int arr[100],out[100];
    rep(i,1,n+1){
        cin>>arr[i];
        m = arr[i];
        out[m] = i; 

    }
    rep(i,1,n+1)
    cout<<out[i]<<" ";
}