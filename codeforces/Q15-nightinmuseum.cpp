#include<iostream>
#include<string.h>
#include<algorithm>

using namespace std;
using ll = long long;
int main()
{
string s;
cin>>s;
ll sum=0;
char start= 'a';
for(int i=0;i<s.size();i++){
    ll l1 = abs(s[i]-start);
    ll l2 = 26 - abs(l1);
    sum += min(l1,l2);
    start = s[i];
}    
cout<<sum<<endl;
} // namespace std;

