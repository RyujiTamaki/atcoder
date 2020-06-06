#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N;
    cin >> N;

    bool ans = false;

    rep(i, 26) {
        rep(j, 15) {
            if (N == 4 * i + 7 * j) {
                ans = true;
                break;
            }
        }
    }

    if (ans) cout << "Yes" << endl;
    else cout << "No" << endl;
}
