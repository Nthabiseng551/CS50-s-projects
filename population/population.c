#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    int n;
    int m;
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

long total;
total = n + round((n/3)) - round((n/4));
printf("%l\n",total);
    // TODO: Print number of years
}
