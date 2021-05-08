#include <iostream>
#include <stdio.h>
#include <time.h>
#include <Windows.h>

using namespace std;

double getCPULoad() {


	FILETIME idle, kernel, user;
	
	GetSystemTimes(&idle, &kernel, &user);
	DWORD last_idle = idle.dwHighDateTime + idle.dwLowDateTime;
	DWORD last_kernel = kernel.dwHighDateTime + kernel.dwLowDateTime;
	DWORD last_user = user.dwHighDateTime + user.dwLowDateTime;

	Sleep(500);

	GetSystemTimes(&idle, &kernel, &user);
	DWORD cur_idle = idle.dwHighDateTime + idle.dwLowDateTime;
	DWORD cur_kernel = kernel.dwHighDateTime + kernel.dwLowDateTime;
	DWORD cur_user = user.dwHighDateTime + user.dwLowDateTime;

	DWORD len_idle = cur_idle - last_idle;
	DWORD len_kernel = cur_kernel - last_kernel;
	DWORD len_user = cur_user - last_user;

	double result = (len_kernel + len_user - len_idle) * 100 / (len_kernel + len_user);

	return result;
}

double getAverage(double * arr, int arrSize) {

	double result = 0;

	for (int i = 0; i < arrSize; i++) {
		result += arr[i];
	}

	result = result / arrSize;

	return result;
}

int main(void) {

	double cl5[5];
	double cl10[10];
	double cl15[15];

	int timer = 0;
	
	double cpuLoad;
	double mean;

	SYSTEMTIME lt;

	while (true) {
		GetLocalTime(&lt);
		cpuLoad = getCPULoad();

		cl5[timer % 5] = cpuLoad;
		cl10[timer % 10] = cpuLoad;
		cl15[timer % 15] = cpuLoad;

		printf("%04d.%02d.%02d %02d:%02d:%02d : ", lt.wYear, lt.wMonth, lt.wDay, lt.wHour, lt.wMinute, lt.wSecond);
		printf("[CPU Load: %6.2f%%] ", cpuLoad);

		if (timer >= 5 - 1) {
			mean = getAverage(cl5, 5);
			printf("[5sec avg: %6.2f%%] ",mean);
		}

		if (timer >= 10 - 1) {
			mean = getAverage(cl10, 10);
			printf("[10sec avg: %6.2f%%] ", mean);
		}

		if (timer >= 15 - 1) {
			mean = getAverage(cl15, 15);
			printf("[15sec avg: %6.2f%%] ", mean);
		}
		printf("\n");

		timer += 1;

		Sleep(500);
	}

	return 0;
}