#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    string S;
    cin >> S;

    int ans = 0;
    rep(i, S.size()) {
        rep(j, S.size() - i) {
            bool is_acgt = false;
            string sub = S.substr(i, j + 1);
            for (char c : sub) {
                if(c == 'A' || c == 'C' || c == 'G' || c == 'T') {
                    is_acgt = true;
                }
                else {
                    is_acgt = false;
                    break;
                }
            }
            if (is_acgt) ans = max(ans, int(sub.size()));
        }
    }
    cout << ans << endl;
}
