#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int average;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int Red = image[i][j].rgbtRed;
            int Green = image[i][j].rgbtGreen;
            int Blue = image[i][j].rgbtBlue;

            average = round(Red + Green + Blue / 3.0);

            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int originalRed, originalGreen; originalBlue;
    int sepiaRed, sepiaGreen, sepiaBlue;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
           originalRed = image[i][j].rgbtRed;
           originalGreen = image[i][j].rgbtGreen;
           originalBlue = image[i][j].rgbtBlue;

           sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue;
           if (sepiaRed > 255)
           {
            image[i][j].rgbtRed = 255;
           }
           else
           {
            image[i][j].rgbtRed = sepiaRed;
           }

           sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue;
           if (sepiaGreen > 255)
           {
            image[i][j].rgbtGreen = 255;
           }
           else
           {
            image[i][j].rgbtGreen = sepiaGreen;
           }

           sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue;
           if (sepiaBlue > 255)
           {
            image[i][j].rgbtBlue = 255;
           }
           else
           {
            image[i][j].rgbtBlue = sepiaBlue;
           }

        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int tmpRed = image[i][j].rgbtRed;
            int tmpGreen = image[i][j].rgbtGreen;
            int tmpBlue = image[i][j].rgbtBlue;

            image[i][j].rgbtRed = image[i][width - j - 1].rgbtRed;
            image[i][j].rgbtGreen = image[i][width - j - 1].rgbtGreen;
            image[i][j].rgbtBlue = image[i][width - j - 1].rgbtBlue;

          // Swapping pixels
            image[i][width - j - 1].rgbtRed = tmpRed;
            image[i][width - j - 1].rgbtGreen = tmpGreen;
            image[i][width - j - 1].rgbtBlue = tmpBlue;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    
    return;
}
