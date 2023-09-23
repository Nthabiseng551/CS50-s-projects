// Implements a dictionary's functionality

#include <cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"


// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 1170; // =(26 * 45): sort buckets alphabetically for first letter then sort by length for each alphabet
int dictionary_size = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int index = hash(word);
    node *cursor = table[index];

    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    char *alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    unsigned int index = 0;
    unsigned int word_length = strlen(word);
    for (int i = 0; i < 26; i++) // Iterate for every letter of the alphabet
    {
        if (toupper(word[0]) == alphabets[i])
        {
            index = (i + (i * LENGTH) -1 )+ word_length ; // index for first letter A from 1 to 45, B from 46 to 91 etc..
        }
    }

    return index;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *open_dictionary = fopen(dictionary, "r");
    if (dictionary == NULL)
    {
        printf("could not open file\n");
        return false;
    }

    char dict_word[LENGTH + 1];

    while (fscanf(open_dictionary, "%s", dict_word) != EOF)
    {
        node *n = malloc(sizeof(node));// New node for each word
        if (n == NULL)
        {
            return false;
        }
        strcpy(n->word, dict_word);
        int index = hash(dict_word);
        n->next = table[index];
        table[index] = n;
        dictionary_size++;
    }
    fclose(open_dictionary);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return dictionary_size;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for(int i = 0; i < N; i++)
    {
        while (table[i] != NULL)
        {
            node *tmp = table[i];
            table[i] = table[i]->next;
            free(tmp);
        }
    }
    return true;
}
