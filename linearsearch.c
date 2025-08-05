#include <stdio.h>
int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++)
        if (arr[i] == key) return i;
    return -1;
}
int main() {
    int arr[] = {2, 4, 6, 8, 10}, key = 8;
    int result = linearSearch(arr, 5, key);
    if (result != -1) printf("Found at index %d", result);
    else printf("Not found");
    return 0;
}
