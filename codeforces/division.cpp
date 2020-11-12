#include<iostream>
using namespace std;
using ll = long long;
int main(){
    ll t;
    ll p,q,a;
    cin>>t;
    while(t>0){
        
        cin>>p>>q;
    
    for(ll x=1;x<p+1;x++){
    if (p%x==0 && x%q != 0){
        cout<<x<<endl;
    }
    }
    t--;

    }
    return 0;
}