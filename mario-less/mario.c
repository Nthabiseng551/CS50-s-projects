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
}