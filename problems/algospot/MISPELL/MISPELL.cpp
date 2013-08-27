#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
using namespace std;
string misspell(int i, string s) {
	string::iterator it=s.begin();
	s.erase(it+=(--i));
	return s;
}
int main() {
	int total=0;
	int index=1;
	string input;
	char str[81];
	getline(cin, input);
	sscanf( input.c_str(), "%d", &total);
	while (total--) {
		int t=0;
		istringstream ins;
		getline(cin, input);
		sscanf(input.c_str(),"%d %s",&t,str);
		string ret = misspell(t, string(str));
		cout << index << " " << ret << endl;
		index++;
	}
}
