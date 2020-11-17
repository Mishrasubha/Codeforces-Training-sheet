#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int main(){
    int n,k;
    cin>>n>>k;
    string al = "abcdefghijklmnopqrstuvwxyz";
    string s2="";
    for(int i=0;i<n;i++){
        s2 += al[i%k];
    }
    cout<<s2;
}