#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N;
    cin >> N;
    vector<int> X(N);
    rep(i, N) cin >> X.at(i);

    sort(X.begin(), X.end());

    int ans = inf;
    for (int i = X.at(0); i <= X.at(N-1); i++) {
        int sum_value = 0;
        for (int j = 0; j < N; j++) {
            sum_value += pow(X.at(j) - i, 2);
        }
        ans = min(ans, sum_value);
    }

    cout << ans << endl;
}
