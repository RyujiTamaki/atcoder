#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int A;
    float B;
    cin >> A >> B;
    int int_B = int(B * 100);
    int AB = A * int_B / 100;
    cout << AB << endl;
}
