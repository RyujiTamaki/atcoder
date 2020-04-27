#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N;
    cin >> N;

    vector<int> vec(N);
    rep(i, N) {
        cin >> vec.at(i);
    }

    sort(vec.begin(), vec.end());
    reverse(vec.begin(), vec.end());

    int alice = 0;
    int bob = 0;

    rep(i, N) {
        if (i % 2 == 0) {
            alice += vec.at(i);
        } else {
            bob += vec.at(i);
        }
    }

    cout << alice - bob << endl;
}
