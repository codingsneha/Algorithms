#include <iostream>

using namespace std;

void insertionSort(int a[], int n) {
    cout << "\nSorting . . . ";
    int key, i, j;
    for (j = 1; j < n; j++) {
        key = a[j];
        i = j - 1;
        while (i >= 0 && a[i] > key) {
            a[i + 1] = a[i];
            i--;
        }
        a[i + 1] = key;
    }
    cout << "Done.";
}
void printArray(int a[], int n) {
    cout << "\n[ ";
    for (int i = 0; i < n; i++)
        cout << a[i] << " ";
    cout << " ]";
}
int main() {
    int n;
    cout << "\nEnter size: "; cin >> n;
    int a[n];
    for (int i = 0; i < n; i++) {
        cout << "\nEnter element[" << i << "]: ";
        cin >> a[i];
    }
    cout << "Your array: ";
    printArray(a, n);
    insertionSort(a, n);
    cout << "\nSorted array: ";
    printArray(a, n);
    return 0;
}