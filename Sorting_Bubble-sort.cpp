#include <iostream>

using namespace std;

void bubbleSort (int a[], int n) {
    int swapped, i, j;
    for (i = 0; i < n; i++) {
        swapped = 0;
        for (j = 0; j < n - i - 1; j++) {
            if (a[j] > a[j + 1]) {
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
                swapped = 1;
            }
            if (!swapped) break;
        }
    }
}

int main() {
    int a[] = {1, 4, 5, 6, 7};
    int n = sizeof(a)/ sizeof(a[0]);
    bubbleSort(a, n);
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    return 0;
}