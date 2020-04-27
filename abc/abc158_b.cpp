#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    long long N, A, B;
    cin >> N >> A >> B;

    if (A == 0) {
        cout << 0 << endl;
        return 0;
    }

    long long ans = N / (A + B) * A;
    long long rem = N % (A + B);
    ans += min(rem, A);

    cout << ans << endl;
}
