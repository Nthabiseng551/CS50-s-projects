//code that implements substitution text cipher

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>



int main(int argc, string argv[])
{

    // Command-line argument exit status
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
//checking if key contains non-alphabetical characters
    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        if (!isalpha(argv[1][i]))
        {
            printf("The key must contain alphabetical characters only.\n");
            return 1;
        }

    }
// checking if key provided is valid/invalid
    int keylength = strlen(argv[1]);
    if (keylength != 26)
    {
        printf("The key must contain 26 characters.\n");
        return 1;
    }



// Checking if key contains all the letters of the alphabet with no repeated characters


    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        if (islower(argv[1][i]))           // Converting key to uppercases
        {
            argv[1][i] = toupper(argv[1][i]);
        }
        else
        {
            argv[1][i] = argv[1][i];
        }
        for (int j = i + 1; j < n; j++)
        {
            if (toupper(argv[1][j]) == argv[1][i])
            {
                printf("Key must not contain repeated characters.\n");
                return 1;
            }
        }
    }




    // Prompting user for plaintext and substituting cipher text

    string plaintext = get_string("plaintext: ");
    printf("ciphertext: ");

    for (int i = 0, l = strlen(plaintext); i < l; i++)
    {
        if (islower(plaintext[i]))
        {
            printf("%c", tolower(argv[1][plaintext[i] - 97]));
        }
        else if (isupper(plaintext[i]))
        {
            printf("%c", toupper(argv[1][plaintext[i] - 65]));
        }
        else
        {
            printf("%c", plaintext[i]);
        }

    }
    printf("\n");
}