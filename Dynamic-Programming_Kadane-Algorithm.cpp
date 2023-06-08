#include <iostream>

using namespace std;

int maxSumSubArray(int a[], int n) {
    int m = INT_MIN, e = 0;
    for (int i = 0; i < n; i++) {
        e += a[i];
        if (m < e) m = e;
        if (e < 0) e = 0;
    }
    return m;
}

int main() {
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++) cin >> a[i];
    cout << "\nMaximum contiguous sum is: " << maxSumSubArray(a, n);
    return 0;
}