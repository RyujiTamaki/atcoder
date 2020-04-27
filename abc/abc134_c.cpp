#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N;
    cin >> N;
    vector<int> A(N), B(N);
    rep(i, N) cin >> A.at(i);
    rep(i, N) B.at(i) = A.at(i);

    sort(B.begin(), B.end());

    int max_v = B.at(N-1);
    int second_v = B.at(N-2);

    for (int a : A) {
        if (a == max_v) cout << second_v << endl;
        else cout << max_v << endl;
    }
}
