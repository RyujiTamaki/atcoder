#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    string s;
    cin >> s;
    string ans = "";
    int i = 1;
    for (char c : s) {
        if (i % 2 != 0) {
            ans += c;
        }
        i++;
    }

    cout << ans << endl;
}
