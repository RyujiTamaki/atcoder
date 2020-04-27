#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)


int f(int n) {
    if (n % 2 == 0) {
        return n / 2;
    }
    return 3 * n + 1;
}

int main() {
    int s;
    cin >> s;

    vector<int> a;

    a.push_back(s);

    for (int i = 1; i < 1000000; i++) {
        int x = f(a.at(i-1));
        a.push_back(x);
        if (count(a.begin(), a.end(), x) == 2) {
            cout << i + 1 << endl;
            return 0;
        }
    }
}
