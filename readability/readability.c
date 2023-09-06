// Code that computes the Coleman-Liau index of text

#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);

int main(void)
{
    string text = get_string("Text: ");
    int nl = count_letters(text);
}

// Function to count letters
int count_letters(string text)
{
    int n = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            n = n + 1;
        }
        else
        {
            n = n + 0;
        }
    }
    return n;
}