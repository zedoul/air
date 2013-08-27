#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
using namespace std;
string lecture(string s) {
	string ret="";
	vector<string> det;
	string::iterator it;
	vector<string>::iterator vit;
	for (it=s.begin();it!=s.end();it+=2) {
		string t;
		t.push_back((*it));
		t.push_back((*(it+1)));
		det.push_back(t);
	}
	
	sort(det.begin(), det.end());
	for (vit=det.begin();vit!=det.end();vit++) {
		ret.push_back((*vit)[0]);
		ret.push_back((*vit)[1]);
	}
	return ret;
}
int main() {
	int total=0;
	string input;
	getline(cin, input);
	sscanf( input.c_str(), "%d", &total);
	while (total--) {
		int t=0;
		istringstream ins;
		getline(cin, input);
		string ret = lecture(input);
		cout << ret << endl;
	}
}
