// Code that computes the Coleman-Liau index of text

#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);
    printf("%i letters\n", letters);
    printf("%i words\n", words);
    printf("%i sentences\n", sentences);


}

// Function to count letters in a text
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

// Function to count words in a text
int count_words(string text)
{
     int n = 1;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == 33 || text[i] == 46 || text[i] == 63)
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


int count_sentences(string text)
{
     int n = 1;
    for (int i = 0; i < strlen(text); i++)
    {
        if (ispunct(text[i]))
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