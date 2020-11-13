#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
using ll = long long;

ll n, x;
ll d;
char y;
 
int main ()
{
    //freopen("test.inp", "r", stdin);
    //freopen("test.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin >> n >> x;
    int res = 0;
    for (int i = 1; i <= n; i++) {
        cin >> y >> d;
        if (y == '+') x+= d;
        else {
            if (x >= d) x-=d;
            else res++;
        }
    }
    cout << x << " "<< res;
}
