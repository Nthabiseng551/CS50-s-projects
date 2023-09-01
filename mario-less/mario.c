// Printing bricks(#) of a right-aligned pyramid of height n
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    // Prompting user for height
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);

    // Printing the pyramid blocks(#)
    for (int i = 1; i <= n; i++)
    {
        for (int j = i; j < n; j++)
        {
            printf(" ");
        }
        for (int k = 1; k <= i; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}