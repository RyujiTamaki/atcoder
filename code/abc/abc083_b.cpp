#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int findSumOfDigits(int n) {
    int sum = 0;
    while (n > 0)
    {
        /* code */
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int main() {
    int N, A, B;
    cin >> N >> A >> B;

    int total = 0;

    rep (i, N + 1) {
        int sum = findSumOfDigits(i);
        if (sum >= A && sum <= B) {
            total += i;
        }
    }
    cout << total << endl;
}
