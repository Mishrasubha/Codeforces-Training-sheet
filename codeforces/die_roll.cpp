#include<iostream>
#include<string.h>
#include<algorithm>
using namespace std;
int main(){
    int y,w,d;
    cin>>y>>w;
    string p[7] = {"", "1/1", "5/6","2/3","1/2","1/3","1/6"};
    d = max(y,w);
    cout<<p[d];
    return 0;
}