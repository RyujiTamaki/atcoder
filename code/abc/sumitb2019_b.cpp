#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N;
    cin >> N;

    bool ans = false;
    int val;
    rep (i, 50000) {
        if (N == int(floor(i * 1.08))) {
            ans = true;
            val = i;
        }
    }

    if (ans) cout << val << endl;
    else cout << ":(" << endl;
}
