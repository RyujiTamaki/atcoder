#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N;
    cin >> N;

    int res = 0;
    int mi = N + 1;
    rep(i, N) {
        int p;
        cin >> p;
        mi = min(mi, p);
        if(mi == p) res++;
    }
    cout << res << endl;
}
