#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    const int n;
    const int m;
    // TODO: Prompt for start size
do
{
    n = get_int("Start size: ");
}
while (n < 9);
    // TODO: Prompt for end size
do
{
    m = get_int("End size: ");
}
while (m < n);
    // TODO: Calculate number of years until we reach threshold

    // TODO: Print number of years
}
