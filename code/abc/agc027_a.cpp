#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N, x;
    cin >> N >> x;
    vector<int> a(N);
    rep(i, N) cin >> a.at(i);

    sort(a.begin(), a.end());

    int ans = 0;

    rep(i, N) {
        if (x >= a[i]) {
            ans++;
            x -= a[i];
        }
    }

    if (ans == N && x > 0) ans--;

    cout << ans << endl;
    return 0;
}
