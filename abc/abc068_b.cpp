#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)


int divideNum(int n) {
    int counter = 0;
    while (n > 0) {
        n /= 2;
        counter++;
    }
    return counter;
}


int main() {
    int N;
    cin >> N;

    int ans = 0;
    int num = 0;

    rep(i, N+1) {
        int divide_num = divideNum(i);
        if (divide_num > num) {
            ans = i;
            num = divide_num;
        }
    }

    cout << ans << endl;
}
