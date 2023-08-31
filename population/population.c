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

int total = n;
int y = 0; //number of years passed
while (total < m)
{
      total = n + round((n/3)) - round((n/4));//total at the end of each year
      n = total;
      y = y + 1;
}
    // TODO: Print number of years
printf("Years: %i\n", y);
}
