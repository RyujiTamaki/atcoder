#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N, M, X;
    cin >> N >> M >> X;
    vector<int> A(M);
    rep(i, M) cin >> A.at(i);

    int right = 0;
    int left = 0;

    rep(i, M) {
        if (A.at(i) > X) {
            right++;
        } else {
            left++;
        }
    }

    cout << min(right, left) << endl;
}
