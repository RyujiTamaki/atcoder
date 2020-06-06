#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int K, N;
    cin >> K >> N;

    vector<int> A(N);
    rep(i, N) cin >> A.at(i);

    int max_distance = 0;

    rep(i, N) {
        int distance;
        if (i == N - 1) {
            distance = K - A.at(i) +  A.at(0);
        } else {
            distance = A.at(i+1) - A.at(i);
        }
        max_distance = max(max_distance, distance);
    }

    cout << K - max_distance << endl;
}
