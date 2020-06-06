#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N, M;
    cin >> N >> M;
    vector<vector<int> > s(M);
    rep(i, M) {
        int k; cin >> k;
        rep(j, k) {
            int a; cin >> a; a--;
            s[i].push_back(a);
        }
    }

    vector<int> p(M);
    rep(i, M) cin >> p[i];

    long long res = 0;

    rep(bit, 1<<N) {
        bool judge = true;
        rep(i, M) {
            int cnt = 0;
            for (int v : s[i]) {
                if(bit & (1<<v)) cnt++;
            }
            if (cnt % 2 != p[i]) judge = false;
        }
        if (judge) res++;
    }
    cout << res << endl;
}
