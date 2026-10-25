#include <stdio.h>

int main(int argc, char const *argv[])
{
    int input;
    while (1)
    {
        printf("ÇëÊäÈë³É¼¨:");
        scanf("%d",&input);
        if (input == -1)
        {
            break;
        }
        else if (input > 100)
        {
            printf("Error\n");
        }
        else if (input >= 90 )
        {
            printf("A\n");
        }
        else if (input >= 80)
        {
            printf("B\n");
        }
        else if (input >= 70)
        {
            printf("C\n");
        }
        else if (input >= 60)
        {
            printf("D\n");
        }
        else if (input >= 0)
        {
            printf("F\n");
        }
        else
        {
            printf("Error\n");
        }
    }
    return 0;
}
