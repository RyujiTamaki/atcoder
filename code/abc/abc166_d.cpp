#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    long long X;
    cin >> X;

    for (long long a = 0; a*a*a*a*a < X; a++) {
        long long b5 = a*a*a*a*a - X;
        for (long long b = 0; b*b*b*b*b <= X; b++) {
            if (b*b*b*b*b == b5) {
                cout << a << " " << b << endl;
                return 0;
            }
        }
        for (long long b = 0; abs(b*b*b*b*b) <= X; b--) {
            if (b*b*b*b*b == b5) {
                cout << a << " " << b << endl;
                return 0;
            }
        }
    }
}
