
#include <stdio.h>
#include <stdlib.h>

struct node
{
    int id;
    int count;
    struct node *next;
};

// Hash function
int hashFunction(int id, int size)
{
    return ((unsigned int)id) % size;
}

// Find the most frequent ID
int findMode(int *sales, int n)
{
    int size = 2 * n + 1;

    struct node **table;
    struct node *temp;

    table = (struct node **)calloc(size, sizeof(struct node *));

    if (table == NULL)
    {
        printf("Memory allocation failed");
        exit(1);
    }

    // Count frequency of each ID
    for (int i = 0; i < n; i++)
    {
        int index = hashFunction(sales[i], size);

        temp = table[index];

        while (temp != NULL)
        {
            if (temp->id == sales[i])
            {
                temp->count++;
                break;
            }

            temp = temp->next;
        }

        // ID not found, create a new node
        if (temp == NULL)
        {
            struct node *newnode;

            newnode = (struct node *)malloc(sizeof(struct node));

            if (newnode == NULL)
            {
                printf("Memory allocation failed");
                exit(1);
            }

            newnode->id = sales[i];
            newnode->count = 1;

            newnode->next = table[index];
            table[index] = newnode;
        }
    }

    // Find the ID with highest frequency
    int maxCount = 0;
    int answer = 0;

    for (int i = 0; i < size; i++)
    {
        temp = table[i];

        while (temp != NULL)
        {
            if (temp->count > maxCount ||
               (temp->count == maxCount && temp->id < answer))
            {
                maxCount = temp->count;
                answer = temp->id;
            }

            temp = temp->next;
        }
    }

    // Free allocated memory
    for (int i = 0; i < size; i++)
    {
        temp = table[i];

        while (temp != NULL)
        {
            struct node *delnode = temp;
            temp = temp->next;
            free(delnode);
        }
    }

    free(table);

    return answer;
}

int main()
{
    int n;

    printf("Enter number of sales: ");
    scanf("%d", &n);

    if (n <= 0)
    {
        printf("Invalid size");
        return 0;
    }

    int *sales;

    sales = (int *)malloc(n * sizeof(int));

    if (sales == NULL)
    {
        printf("Memory allocation failed");
        return 0;
    }

    printf("Enter product IDs:\n");

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &sales[i]);
    }

    printf("Most frequent product ID = %d\n", findMode(sales, n));

    free(sales);

    return 0;
}
