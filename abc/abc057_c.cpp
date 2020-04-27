#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll=long long


int count_digits(ll N){
    int digits = 0;

    while(N>0){
        N/=10;
        digits++l
    }
    return digits;
}

int main() {
    ll N;
    cin >> N;

    int ans = count_digits(N);

    for(ll A=1LL; A*A<=N; ++A){
        if(N % A != 0) continue;
        const ll B = N / A;

        const int cur = max(count_digits(A), count_digits(B));

        if (ans > cur) {
            ans = cur;
        }
    }
    cout << ans << endl;
}
