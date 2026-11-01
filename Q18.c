
#include <stdio.h>
#include <stdlib.h>

void reverseSubsegment(int *arr, int start, int end)
{
    int temp;

    while (start < end)
    {
        temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;

        start++;
        end--;
    }
}

int main()
{
    int n, start, end;

    int *arr;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    arr = (int *)malloc(n * sizeof(int));

    if (arr == NULL)
    {
        printf("Memory allocation failed");
        return 0;
    }

    printf("Enter array elements:\n");

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    printf("Enter start index: ");
    scanf("%d", &start);

    printf("Enter end index: ");
    scanf("%d", &end);

    reverseSubsegment(arr, start, end);

    printf("Array after reversing sub-segment:\n");

    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }

    free(arr);

    return 0;
}
