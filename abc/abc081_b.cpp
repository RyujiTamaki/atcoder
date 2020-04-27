#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N;
    int A[210];
    cin >> N;
    rep(i, N) {
        cin >> A[i];
    }

    int res = 0;

    while (true)
    {
        /* code */
        bool is_odd = false;

        rep(i, N) {
            if(A[i] % 2 != 0) is_odd = true;
        }

        if (is_odd) break;

        rep(i, N) {
            A[i] /= 2;
        }

        res++;
    }

    cout << res << endl;
}
