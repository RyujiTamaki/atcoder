#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> A(M), B(M);
    for (int i = 0; i < M; i++) {
        cin >> A.at(i) >> B.at(i);
    }

    // ここにプログラムを追記
    // (ここで"試合結果の表"の2次元配列を宣言)
    vector<vector<char>> table(N, vector<char>(N, '-'));

    rep(i, M) {
        // 1〜N → 0〜N-1 に変換
        A.at(i)--; B.at(i)--;
        table.at(A.at(i)).at(B.at(i)) = 'o';  // AはBに勝った
        table.at(B.at(i)).at(A.at(i)) = 'x';  // BはAに負けた
    }

    rep(i, N) {
        rep(j, N) {
            cout << table.at(i).at(j);
            if (j == N - 1) {
                cout << endl;  // 行末なら改行
            }
            else {
                cout << " ";
            }
        }
    }
}
