#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <cassert>
#include <cstring>
using namespace std;

int cache[501][501];
int lis(vector<int> tokens) {
	memset(cache,-1,sizeof(cache));
	int longest = 0;
	for (int i=0;i<tokens.size();i++) {
		for (int j=0;j<tokens.size();j++) {

		}
	}
	return longest;
}

int main() {
	int total=0;
	int casecount = 0;
	int ret = 0;
	string input;
	getline(cin, input);
	sscanf( input.c_str(), "%d", &total);
	while (total--) {
		getline(cin, input);
		sscanf( input.c_str(), "%d", &casecount);
		getline(cin, input);
		string buf;
		stringstream ss(input);
		vector<int> tokens;
		while (ss >> buf && casecount--) {
			int det;
			sscanf( buf.c_str(), "%d", &det);
			tokens.push_back(det);
		}
		ret = lis(tokens);
		cout << ret << endl;
	}
}
