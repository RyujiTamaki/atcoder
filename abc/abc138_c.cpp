#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N;
    cin >> N;
    vector<double> v(N);
    rep(i, N) cin >> v.at(i);

    sort(v.begin(), v.end());
    double ans = (v.at(0) + v.at(1)) / 2;
    for (int i = 2; i < N; i++) {
        ans = (ans + v.at(i)) / 2;
    }
    cout << ans << endl;
}
