#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N, A;
    cin >> N >> A;

    if ((N % 500) <= A) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}
