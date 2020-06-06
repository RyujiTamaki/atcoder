#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    string S;
    cin >> S;
    int N = S.size();
    string ans = "yes";
    for(int i = 0; i < N; i++) {
        for(int j = i + 1; j < N; j++) {
            if(S[i] == S[j]) {
                ans == "no";
                break;
            }
        }
    }

    cout << ans << endl;
}
