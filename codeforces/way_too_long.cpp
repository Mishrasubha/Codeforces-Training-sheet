
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
 
int main() {
    long long n;
    cin>>n;
    char a[10000];
    for (long long i=1;i<=n;i++){
       cin>>a;
       if (strlen(a)>10) {
                cout<<a[0];
                cout<<strlen(a)-2;
                cout<<a[strlen(a)-1]<<endl;
            }
       else cout<<a<<endl;
    }
}