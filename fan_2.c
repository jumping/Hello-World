#include <stdio.h>
int g(int x, int y)
{
    return x+y;
}

int f(int x, int y)
{
    {static int x = 2;
    printf("@ First x: %d \n",x);
    if(y>2)
    { x=x*x;
      y=x;
    }
    else y=x+1;
    }
    printf("@ End x: %d \n",x);
    printf("y is %d \n",y);
    return x+y;
}

void main()
{
    int a = 3;
    printf("%d\n", g(a,2));
    printf("%d\n", f(a,3));
    printf("%d\n", f(a,2));
}

