#include <iostream>
#include <cmath>
using namespace std;
int main() 
{
  double num, result;
  num = 1.12;
  result = round(num);
  cout << "round(" << num << ") = " << result << endl;
  num = 3.82;
  result = round(num);
  cout << "round(" << num << ") = " << result << endl;
  num = 5.5;
  result = round(num);
  cout << "round(" << num << ") = " << result;
  return 0;
}
