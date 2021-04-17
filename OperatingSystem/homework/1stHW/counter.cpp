#include <Windows.h>
#include <Psapi.h>
#include <iostream>
#include <time.h>

using namespace std;

int main(void)
{   
   DWORD aProcesses[1024];
   DWORD cbNeeded;
   DWORD cProcesses;

   SYSTEMTIME lt;
   
   int timer = 0;

   while (timer < 600) 
   {
      GetLocalTime(&lt);
      if (EnumProcesses(aProcesses, sizeof(aProcesses), &cbNeeded)) {
         cProcesses = cbNeeded / sizeof(DWORD);
         printf("%04d.%02d.%02d %02d:%02d:%02d : %d\n", lt.wYear, lt.wMonth, lt.wDay, lt.wHour, lt.wMinute, lt.wSecond, cProcesses);
         timer += 1;
         Sleep(1000);
      }
   }

   return 0;
}