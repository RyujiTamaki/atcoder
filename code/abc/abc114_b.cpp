#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    string S;
    cin >> S;

    int min_diff = 999;
    for (int i = 0; i < S.size() - 2; i++) {
        int X = stoi(S.substr(i, 3));
        int diff = abs(X - 753);
        min_diff = min(min_diff, diff);
    }
    cout << min_diff << endl;
}
