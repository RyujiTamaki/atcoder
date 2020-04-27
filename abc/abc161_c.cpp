#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    long long N, K;
    cin >> N >> K;

    long long t = N % K;
    cout << min(t, K - t) << endl;
}
