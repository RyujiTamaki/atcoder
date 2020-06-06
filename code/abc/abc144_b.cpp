#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N;
    cin >> N;
    bool can = false;
    rep(i, 9) {
        rep(j, 9) {
            if ((i + 1) * (j + 1) == N) can = true;
        }
    }
    if (can) cout << "Yes" << endl;
    else cout << "No" << endl;
}
