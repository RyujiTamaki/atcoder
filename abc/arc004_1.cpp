#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N;
    cin >> N;

    vector<int> x(N), y(N);
    rep(i, N) {
        cin >> x.at(i) >> y.at(i);
    }

    double max_distance = 0;
    rep(i, N) {
        rep(j, N) {
            double distance = sqrt(pow((x.at(i) - x.at(j)), 2) + pow((y.at(i) - y.at(j)), 2));
            max_distance = max(max_distance, distance);
        }
    }

    cout << max_distance << endl;
}
