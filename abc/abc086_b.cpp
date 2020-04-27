#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)


int main() {
    string a, b;
    cin >> a >> b;
    int x = stoi(a+b);
    for (int i = 0; i <= 1000; i++) {
        if (i*i == x) {
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
}
