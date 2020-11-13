#include<iostream>
using namespace std;
using ll = long long;
int main(){
    ll n,b,d,sums;
    cin>>n>>b>>d;
    ll w=0;
    ll a[1000000];
    for(int i=0;i<n;i++){
        cin>>a[i];
        if(a[i]<=b){
        
         
         sums += a[i];}
         if(sums>d){
             w++;
             sums = 0;
         }
         }
cout<<w;}