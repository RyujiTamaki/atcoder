#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    string s;
    cin >> s;
    int counter = 0;
    rep(i, s.size()) {
        if (s[i] == '1') ++counter;
    }
    cout << counter << endl;
}
