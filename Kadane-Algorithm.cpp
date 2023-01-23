long long maxSubarraySum(int a[], int n){
        long long int m = INT_MIN, e = 0;
        for (int i = 0; i < n; i++) {
            e = e + a[i];
            if (m < e) m = e;
            if (e < 0) e = 0;
        }
        return m;
}