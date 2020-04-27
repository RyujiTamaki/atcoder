#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int eat_num(int Ai, int D) {
    return (D - 1) / Ai + 1;
}

int main() {
    int N, D, X;
    cin >> N >> D >> X;
    vector<int> A(N);
    rep(i, N) cin >> A.at(i);

    int eat = 0;

    rep(i, N) {
        eat += eat_num(A.at(i), D);
    }

    cout << eat + X << endl;
}
