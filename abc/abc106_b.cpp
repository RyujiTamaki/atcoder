#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

bool isPalindromic(int n) {
    if (n % 2 == 0) return false;
    int counter = 0;
    rep(i, n+1) {
        if (n % (i+1) == 0) counter++;
    }
    return counter == 8;
}

int main() {
    int N;
    cin >> N;
    int counter = 0;
    rep(i, N) {
        if (isPalindromic(i+1)) counter++;
    }
    cout << counter << endl;
}
