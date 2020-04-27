#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N;
    string S;
    cin >> N >> S;

    int counter = 0;
    rep(i, N-2) {
        if (S.substr(i, 3) == "ABC") counter++;
    }
    cout << counter << endl;
}
