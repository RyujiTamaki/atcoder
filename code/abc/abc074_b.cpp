#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N, K;
    cin >> N >> K;
    vector<int> x(N);
    rep(i, N) cin >> x.at(i);

    int distance = 0;
    rep(i, N) {
        int a_distance = x.at(i);
        int b_distance = abs(K - x.at(i));
        distance += min(a_distance, b_distance);
    }

    cout << distance * 2 << endl;
}
