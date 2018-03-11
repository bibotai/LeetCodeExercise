#include <stdio.h>
#include   <string.h>
char *str1[] = {"abcdefg12345dsfa","abcdefg12345qwer","abcdefg1234wqerrte"};
int longestCommonPrefix(char *strs[])
{
    int i = 0;
    int j = 0;
    int len = 0;
    int mid = 0;
    int right = 0;
    int left = 0;
    while (strs[i])//计算字符串数组的个数
    {
        i++;
    }
    for(j = 1 ;j < i;j++)
    {
        right = strlen(strs[j]);
        left = 0;
        while(left<=right)//二分法比较
        {
            mid = (left+right)/2;
            if(strncmp(strs[j],strs[j-1],mid) != 0)
            {

                right = mid-1;
            }
            else
            {
                left = mid+1;
            }
        }
        if(len == 0 || len >right)
        {
            len = right;
        }
        printf("%d\n",len);
    }
    return len;
}
int main(void) {
    int a = 0;
    int b= 0 ;
    char c[100] = {};
	a = longestCommonPrefix(str1);
    memcpy(c,*str1,a);

    printf("%s\n",c);
}