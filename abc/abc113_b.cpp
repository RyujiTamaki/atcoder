#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N, T, A;
    cin >> N >> T >> A;
    vector<int> H(N);
    rep(i, N) {
        cin >> H.at(i);
    }

    float min_diff = 10000000;
    int min_index;

    vector<float> temp(N);
    rep(i, N) {
        float temp = T - H.at(i) * 0.006;
        float diff = abs(temp - A);
        if (min_diff > diff) {
            min_diff = diff;
            min_index = i;
        }
    }

    cout << min_index + 1 << endl;
}
