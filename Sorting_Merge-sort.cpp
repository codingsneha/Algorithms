    void merge(int arr[], int l, int m, int r) {
        auto const n1 = m - l + 1;
        auto const n2 = r - m;
        
        auto *L = new int[n1];
        auto *R = new int[n2];

        for (auto i = 0; i < n1; i++)
            L[i] = arr[l + i];
        for (auto j = 0; j < n2; j++)
            R[j] = arr[m + 1 + j];
        auto i1 = 0, i2 = 0, i = l;

        while(i1 < n1 && i2 < n2) {
            if (L[i1] <= R[i2])
                arr[i] = L[i1++];
            else
                arr[i] = R[i2++];
            i++;
        }
        while (i1 < n1)
            arr[i++] = L[i1++];

        while (i2 < n2)
            arr[i++] = R[i2++];

        delete[] L;
        delete[] R;
    }
    void mergeSort(int arr[], int const begin, int const end){
        if (begin >= end)
            return;
        auto mid = begin + (end - begin) / 2;
        mergeSort(arr, begin, mid);
        mergeSort(arr, mid + 1, end);
        merge(arr, begin, mid, end);
    }