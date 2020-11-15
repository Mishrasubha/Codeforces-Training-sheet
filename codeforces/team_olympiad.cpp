#include<iostream>
#include<algorithm>
#include<vector>
#include<list>
using ll = long long;
using namespace std;
int main(){
    int n,n1=0,n2=0,n3=0;
    int ib[5000];
    int i2[5000];
    int i3[5000];
    cin>>n;
    int a[5000];
    int t1=0,t2=0,t3=0;
    for(int i=1;i<=n;i++){
        cin>>a[i];
        if(a[i]==1){
            n1++;
            ib[t1]=i;
            t1++;
        }
        if(a[i]==2){
            n2++;
            i2[t2]= i;
            t2++;
        }
        if(a[i]==3){ n3++;
        i3[t3] = i;
        t3++ ;}
    }
    int t=0,to=0;
    t = min(n1,min(n2,n3));
    cout<<t<<endl;
    for(int i=0;i<t;i++){
        cout<<ib[i]<<" "<<i2[i]<<" "<<i3[i]<<endl;
    }
}