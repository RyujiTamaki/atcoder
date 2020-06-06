#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int A, B, C, X, Y;
    cin >> A >> B >> C >> X >> Y;
    int ans = A * X + B * Y;

    for (int i = 1; i <= 100000; i++) {
        int total = 2 * C * i + A * max(0, X-i) + B * max(0, Y-i);
        ans = min(total, ans);
    }

    cout << ans << endl;
}
