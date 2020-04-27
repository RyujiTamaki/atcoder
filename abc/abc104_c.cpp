#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int D;
long long G;
vector<long long> p, c;

int main() {
    cin >> D >> G;
    p.resize(D), c.resize(D);
    rep(i, D) cin >> p.at(i) >> c.at(i);

    long long res = 1 << 29;
    rep(bit, (1<<D)) {
        long long sum = 0;
        long long num = 0;
        rep(i, D) {
            if(bit & (1<<i)) {
                sum += c[i] + p[i] * 100 * (i+1);
                num += p[i];
            }
        }
        if (sum >= G) {
            res = min(res, num);
        }
        else {
            for (int i = D - 1; i >=0; i--) {
                if (bit & (1 <<i)) continue;
                for (int j = 0; j< p[j]; j++) {
                    if (sum >= G) break;
                    sum += 100 * (i+1);
                    num++;
                }
            }
            res = min(res, num);
        }
    }
    cout << res << endl;
}
