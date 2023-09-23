#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover card.raw\n");
        return 1;
    }

    // Open memory card for reading
    FILE *raw_file = fopen(argv[1], "r");

    if (raw_file == NULL)
    {
        printf("Could not open file\n");
        return 1;
    }

    BYTE buffer[512];   // Variable to store 512 chunks of array
    int count_jpeg = 0; // count jpeg files(images) found
    FILE *output_file = NULL;

    char filename[8];

    // Read into the buffer until end of card
    while (fread(buffer, 1, 512, raw_file) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            sprintf(filename, "%03i.jpg", count_jpeg++);
            output_file = fopen(filename, "w");
        }
        if (output_file != NULL)
        {
            fwrite(buffer, 1, 512, output_file);
        }
    }
    fclose(raw_file);
    fclose(output_file);
    return 0;
}