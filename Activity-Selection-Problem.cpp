#include <iostream>
using namespace std;

class Activity {
    public:
        int start, finish;
};

void sortActivities(Activity a[], int n) {
    bool swapped;
    for (int i = 0; i < n; i++) {
        swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (a[j].finish > a[j + 1].finish) {
                Activity temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
                swapped = true;
            }
        }
        if (!swapped) break;
    }
}
void printActivities(Activity a[], int n) {
    int i = 0;
    cout << "(" << a[i].start << ", " << a[i].finish << ")" << endl;
    for (int j = 1; j < n; j++) {
        if (a[j].start >= a[i].finish) {
            cout << "(" << a[j].start << ", " << a[j].finish << ")" << endl;
            i = j;
        }
    }
}
int main() {
    Activity a[100];
    int n, i, j;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a[i].start >> a[i].finish;
    }
    
    sortActivities(a, n);
    printActivities(a, n);
    return 0;
}