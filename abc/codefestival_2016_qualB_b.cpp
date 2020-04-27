#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N, A, B;
    cin >> N >> A >> B;
    string S;
    cin >> S;

    int num = 0;
    int b_num = 0;

    for (char c : S) {
        bool ans = false;
        if (c == 'a') {
            if (A + B > num) {
                ans = true;
                num++;
            }
        }
        else if (c == 'b') {
            if (A + B > num && b_num < B) {
                ans = true;
                num++;
                b_num++;
            }
        }

        if (ans) cout << "Yes" << endl;
        else cout << "No" << endl;
    }
}
