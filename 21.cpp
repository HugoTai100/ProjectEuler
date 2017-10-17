#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int check(int x)
{
  int ans = 0;
  int i = 1;
  while(i < x)
  {
    if ( x % i == 0 )
      ans += i;
    ++i;
  }
  return ans;
}
int main()
{
  int temp1, temp2;
  int ans = 0;
  for(int i = 0; i < 1e4; ++i)
  {
    temp1 = check(i);
    temp2 = check(temp1);
    if (temp2 == i && i != temp1)
      ans += i;


  }
  cout << ans << endl;
}

