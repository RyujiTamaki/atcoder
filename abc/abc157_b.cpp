#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    vector<vector<int>> A(3, vector<int>(3));
    rep(i, 3) {
        rep(j, 3) {
            cin >> A.at(i).at(j);
        }
    }

    int N;
    cin >> N;

    vector<int> B(N);
    rep(i, N) {
        cin >> B.at(i);
    }

    vector<vector<bool>> C(3, vector<bool>(3, false));
    rep(i, 3) {
        rep(j, 3) {
            rep(k, N) {
                if(A.at(i).at(j) == B.at(k)) C.at(i).at(j) = true;
            }
        }
    }

    string ANS = "No";
    rep(i, 3) {
        if(C.at(i).at(0) and C.at(i).at(1) and C.at(i).at(2)) ANS = "Yes";
    }
    rep(i, 3) {
        if(C.at(0).at(i) and C.at(1).at(i) and C.at(2).at(i)) ANS = "Yes";
    }
    if(C.at(0).at(0) and C.at(1).at(1) and C.at(2).at(2)) ANS = "Yes";
    if(C.at(2).at(0) and C.at(1).at(1) and C.at(0).at(2)) ANS = "Yes";

    cout << ANS << endl;;
}
