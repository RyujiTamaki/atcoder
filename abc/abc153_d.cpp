#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

long long f(long long H) {
    if (H == 1) return 1;
    return 2 * f(H / 2) + 1;
}

int main() {
    long long H;
    cin >> H;

    cout << f(H) << endl;
}
