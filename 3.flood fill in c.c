#include <stdio.h>
#include <conio.h>
#include <graphics.h>

void FF(int x, int y, int f_c, int default_c)  
{  
    if (getpixel(x, y) == default_c)  
    {  
        putpixel(x, y, f_c);   
        FF(x, y + 1, f_c, default_c);  
        FF(x, y - 1, f_c, default_c);  
        FF(x + 1, y, f_c, default_c);  
        FF(x + 1, y + 1, f_c, default_c);  
        FF(x + 1, y - 1, f_c, default_c);  
        FF(x - 1, y, f_c, default_c);  
        FF(x - 1, y + 1, f_c, default_c);  
        FF(x - 1, y - 1, f_c, default_c);  
    }  
}  

int main() 
{     
    int gd = DETECT, gm;     
    initgraph(&gd, &gm, "C:/TURBOC3/bgi");  
    
    rectangle(25, 25, 50, 50);  
    
    FF(26, 26, RED, BLACK);  
    
    getch(); 
    closegraph();  
    return 0;  
}
