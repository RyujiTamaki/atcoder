#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int  N;
    cin >> N;
    vector<int> A(N);
    rep(i, N) cin >> A.at(i);

    vector<int> B(N);
    rep(i, N) B.at(A.at(i) - 1) = i + 1;
    rep(i, N) cout << B.at(i) << " ";
    cout << endl;
}
