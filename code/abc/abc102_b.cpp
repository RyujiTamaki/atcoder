#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N;
    cin >> N;
    vector<int> A(N);

    rep(i, N) {
        cin >> A.at(i);
    }

    cout << abs(*max_element(A.begin(), A.end()) - *min_element(A.begin(), A.end())) << endl;
}
