#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    long long a, b;
    cin >> a >> b;

    if (a <= 0 and b >= 0) {
        cout << "Zero" << endl;
        return 0;
    }

    if (a > 0) cout << "Positive" << endl;

    if (a <= 0 and b < 0) {
        long long c = b - a + 1;
        if (c % 2 == 0) cout << "Positive" << endl;
        else cout << "Negative" << endl;
    }
}
