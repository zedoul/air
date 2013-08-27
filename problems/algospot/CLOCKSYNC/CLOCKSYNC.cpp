#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <cassert>
using namespace std;

#define INF32 99999
#define SWITCHES 10
#define CLOCKS 16
#define SWITCH_CONTROL 4

const char linked[SWITCHES][CLOCKS+1] = {
	"xxx.............",
	"...x...x.x.x....",
	"....x.....x...xx",
	"x...xxxx........",
	"......xxx.x.x...",

	"x.x...........xx",
	"...x..........xx",
	"....xx.x......xx",
	".xxxxx..........",
	"...xxx...x...x.."
};

void clock_print (vector<int>& clocks) {
	cout << "clock: ";
	for (int i=0;i<clocks.size();i++) {
		cout << clocks[i] << " ";
	}
	cout << endl;
}

bool aligned(vector<int>& clocks) {
	for (int i=0;i<clocks.size();i++){
		if (12 != clocks[i]) {
			return false;
		}
	}
//	clock_print(clocks);
	return true;
}

void clock_fix(vector<int>& clocks, int swi) {
	for (int i=0;i<CLOCKS;i++) {
		if ('x' == linked[swi][i]) {
			clocks[i] += 3;
			if (12 < clocks[i]) {
				clocks[i] -= 12;
			}
		}
	}
}

int _clocksync(vector<int>& clocks, int ci) {
	int ret = INF32;
	if (ci == SWITCHES) {
		return aligned(clocks) ? 0 : INF32;
	}
	for (int i=0;i<SWITCH_CONTROL;i++) {
		ret = min(ret,  _clocksync(clocks, ci+1)+i);
		clock_fix(clocks, ci);
	}
	return ret;
}

int clocksync(vector<int>& clocks) {
	return _clocksync(clocks, 0);
}

int main() {
	int total=0;
	int ret=0;
	string input;
	getline(cin, input);
	sscanf(input.c_str(), "%d", &total);
	while (total--) {
		vector<int> clocks;
		getline(cin, input);
		stringstream ss(input);
		string buf;
		while (ss >> buf) {
			int det;
			sscanf(buf.c_str(), "%d", &det);
			clocks.push_back(det);
		}
//		clock_print(clocks);
		ret = clocksync(clocks);
		if (ret == INF32) ret = -1;
		cout << ret << endl;
	}
}

