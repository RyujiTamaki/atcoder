#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

string S;

int dfs(int i, int sum) {
    if (i == S.size()) {
        cout << "i: " << i << " sum: " << sum << endl;
        return sum;
    }
    cout << "i: " << i << " sum: " << sum << endl;
    return dfs(i + 1, sum * 10 + (S[i] - '0')) + dfs(i + 1, sum + (S[i] - '0'));
}

int main() {
    cin >> S;
    cout << dfs(0, 0) << endl;
}
