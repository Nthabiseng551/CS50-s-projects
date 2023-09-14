#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;

            int average = round((red + green + blue) / 3.0);

            image[i][j].rgbtRed = image[i][j].rgbtGreen = image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int sepiaRed, sepiaGreen, sepiaBlue;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
          int originalRed = image[i][j].rgbtRed;
          int originalGreen = image[i][j].rgbtGreen;
          int originalBlue = image[i][j].rgbtBlue;

           sepiaRed = round( .393 * originalRed + .769 * originalGreen + .189 * originalBlue);
           if (sepiaRed > 255)
           {
            image[i][j].rgbtRed = 255;
           }
           else
           {
            image[i][j].rgbtRed = sepiaRed;
           }

           sepiaGreen = round( .349 * originalRed + .686 * originalGreen + .168 * originalBlue);
           if (sepiaGreen > 255)
           {
            image[i][j].rgbtGreen = 255;
           }
           else
           {
            image[i][j].rgbtGreen = sepiaGreen;
           }

           sepiaBlue = round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue);
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
        for (int j = 0; j < width/2; j++)
        {
            int tmpRed = image[i][j].rgbtRed;
            int tmpGreen = image[i][j].rgbtGreen;
            int tmpBlue = image[i][j].rgbtBlue;

            image[i][j].rgbtRed = image[i][width - (j + 1)].rgbtRed;
            image[i][j].rgbtGreen = image[i][width - (j + 1)].rgbtGreen;
            image[i][j].rgbtBlue = image[i][width - (j + 1)].rgbtBlue;

          // Swapping pixels
            image[i][width - (j + 1)].rgbtRed = tmpRed;
            image[i][width - (j + 1)].rgbtGreen = tmpGreen;
            image[i][width - (j + 1)].rgbtBlue = tmpBlue;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int totalRed, totalGreen, totalBlue;
            totalRed = totalGreen = totalBlue = 0;
            int counter = 0;

        
    return;
}
