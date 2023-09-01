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
    printf("Stored: %i\n", n);

    // Printing the pyramid blocks(#)
     for (int i = 1; i <= n; i++)
         {
            for (int j = 1; j <= i; j++)
            {
                printf ("#");
            }
            printf("\n");
         }
}