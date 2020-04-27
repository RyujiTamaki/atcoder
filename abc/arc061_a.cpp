#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define ll long long

int main() {
    string S;
    cin >> S;

    int N = S.size();
    ll ans = 0;
    rep(i, (1 << (N - 1))) {
        ll t = S[0] - '0';
        rep(j, N - 1) {
            if (i & (1 << j)) {
                ans += t;
                t = S[j+1] - '0';
            } else {
                t *= 10;
                t += S[j+1] - '0';
            }
        }
        ans += t;
    }

    cout << ans << endl;
}
