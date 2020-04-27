#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using pint = pair<int, int>;

int N;
vector<vector<pint>> v;

bool judge(int bit) {
    // i 人目の証言を検証する
    for (int i = 0; i < N; ++i) {
        if ( !(bit & (1 << i)) ) continue;
        for (pint xy : v[i]) {
            int x = xy.first; // x が
            int y = xy.second; // y = 1: 正直、y = 0: 不親切

            // y = 1 なのに「不親切」だったらダメ
            if (y == 1 && !(bit & (1 << x))) return false;

            // y = 0 なのに「正直者」だったらダメ
            if (y == 0 && (bit & (1 << x))) return false;
        }
    }
    return true;
}

int main() {
    cin >> N;
    v.resize(N);
    rep(i, N) {
        int A; cin >> A;
        v[i].resize(A);
        rep(j, A) {
            cin >> v[i][j].first >> v[i][j].second;
            v[i][j].first--;
        }
    }

    int res = 0;
    rep(bit, (1<<N)) {
        if(judge(bit)) {
            int count = 0;
            rep(i, N) {
                if (bit & (1<<i)) count++;
            }
            res = max(res, count);
        }
    }
    cout << res << endl;
}
