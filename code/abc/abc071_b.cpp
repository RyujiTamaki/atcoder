#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    string S;
    cin >> S;
    vector<bool> app(26, false);

    for (char c : S) {
        app.at(c - 'a') = true;
    }

    rep (i, 26) {
        if (!app.at(i)) {
            cout << (char)(i + 'a') << endl;
            return 0;
        }
    }

    cout << "None" << endl;
}
