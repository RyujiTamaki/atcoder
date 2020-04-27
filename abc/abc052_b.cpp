#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N;
    string S;
    cin >> N >> S;
    int x = 0;
    int ans = 0;

    for (char c : S) {
        if (c == 'I') x++;
        else x--;
        ans = max(x, ans);
    }

    cout << ans << endl;
}
