#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
using namespace std;

string encrypt(string input) {
	string a, b;
	for (int index=0;index<input.size();index++) {
		char it = input[index];
		if (0 != index%2) {
			a.push_back(it);
		} else {
			b.push_back(it);
		}
	}
	return b+a;
}

int main() {
	int total=0;
	int casecount = 0;
	string ret;
	string input;
	getline(cin, input);
	sscanf( input.c_str(), "%d", &total);
	while (total--) {
		getline(cin, input);
		ret = encrypt(input);
		cout << ret << endl;
	}
}
