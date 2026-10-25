#include <stdio.h>
int average(int a[],int length)
{
    int sum = 0;
    double ave;
    for(int i = 0;i < length;i ++)
    {
    sum = sum + a[i];
    ave = sum / (double)length;
    }
    return ave;
}

int main(void)
{
    int n;
    int arr[100];
    double a;
        printf("请输入数字个数:");
        scanf("%d",&n);
        printf("请输入%d个数字(以空格或回车分隔):",n);
            for(int i = 0;i < n;i ++)
            {
            scanf("%d",&arr[i]);
            }
                a = average(arr,n);
                printf("%.2f",a);
}
