#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int n, k;
vector<int> a(4);

bool dfs(int i, int sum) {
    // n個決め終わったら、今までの和sumがkと等しいかを返す
    if (i == n) return sum == k;

    // a[i]を使わない場合
    if (dfs(i + 1, sum)) return true;

    // a[i]を使う場合
    if (dfs(i + 1, sum + a[i])) return true;

    // a[i]を使う使わないに拘らずkが作れないのでfalseを返す
    return false;
}

int main() {
    cin >> n;
    rep(i, n) cin >> a.at(i);
    cin >> k;
    if (dfs(0, 0)) printf("Yes\n");
    else printf("No\n");
}
