#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

bool isEven(int n) {
    return n % 2 == 0;
}

int main() {
    int A, B, C;
    cin >> A >> B >> C;

    if (A == B and B == C and isEven(A)) {
        cout << -1 << endl;
        return 0;
    }

    int num = 0;
    bool can = true;

    while(can) {
        if (isEven(A) && isEven(B) && isEven(C)) {
            int tmpA = (B + C) / 2;
            int tmpB = (A + C) / 2;
            int tmpC = (A + B) / 2;
            A = tmpA;
            B = tmpB;
            C = tmpC;
            num++;
        } else {
            can = false;
        }
    }

    cout << num << endl;
}
