#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)


bool is_prime(int x) {
    if (x <= 1) return false;

    for (int i = 2; i * i <= x; i++) {
        if (x % i == 0) return false;
    }
    return true;
}

int main() {
    int X;
    cin >> X;

    int p = X;
    while (!is_prime(p))
    {
        p++;
    }
    cout << p << endl;
}
