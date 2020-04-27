#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N;
    cin >> N;
    vector<int> P(N), Q(N);
    rep(i, N) {
        cin >> P.at(i);
        P.at(i)--;
    }
    rep(i, N) {
        cin >> Q.at(i);
        Q.at(i)--;
    }

    map<vector<int>, int> ord;
    int iter = 0;

    vector<int> v(N);
    for (int i = 0; i < N; ++i) v[i] = i;

    do {
        ord[v] = iter++;
    } while (next_permutation(v.begin(), v.end()));

    cout << abs(ord[P] - ord[Q]) << endl;
}
