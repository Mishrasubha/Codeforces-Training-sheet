#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;
using ll = long long;
int main(){
    int n,t,k,d;
    cin>>n>>t>>k>>d;
    int curr=0;
    while(curr<=d){
        n -= k;
        curr += t;
    }
    if(n>0){
        cout<<"YES";
    }
    else
    {
        cout<<"NO";
    }
}
    