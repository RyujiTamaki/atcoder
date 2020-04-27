#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    int a = x2 - x1;
    int b = y2 - y1;
    cout << x2 - b << " " <<  y2 + a << " " << x1 - b << " " << y1 + a << endl;
}
