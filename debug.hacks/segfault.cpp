#include <stdio.h>

int main(void)
{
  int *a = NULL;
  *a = 0x1;   // cause segment fault
  return 0;
}
