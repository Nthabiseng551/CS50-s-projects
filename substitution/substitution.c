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


    for (int i = 0,n = strlen(argv[1]); i < n; i++)
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
        if(toupper(argv[1][j]) == argv[1][i])
        {
            printf("Key must not contain repeated characters.\n");
            return 1;
        }
        }
     }




    // Prompting user for plaintext and encrypting it
    string alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string plaintext = get_string("plaintext: ");
    printf("ciphertext: ");

    for (int i = 0,l = strlen(plaintext); i < l; i++)
    {
            for(int j = 0, m = 26; j < m; j++)
            {
             if (isupper(plaintext[i]) && plaintext[i] == alphabets[j] )
        {
            printf("%c", toupper(argv[1][j]));
        }
            else if (islower(plaintext[i]) && plaintext[i] == (alphabets[j] + 32))
        {
            printf("%c", tolower(argv[1][j]));
        }
            printf("%c", plaintext[i]);

            }
    }
    printf("\n");

}
