#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <cassert>
#include <cstring>
using namespace std;

void _print(vector<string> target) {
	for (int i=0;i<target.size();i++) {
		cout <<target[i]<<endl;
	}
}

int cache[101][101];
bool _wildcard(string pattern, string target, int p, int t) {
	int& ret = cache[p][t];
	//1. memoisation
	if (-1 != ret) {
		return ret; 
	}

	while (p < pattern.size() && t < target.size() && 
		(pattern[p] == '?' || pattern[p] == target[t] )) {
		p++;
		t++;
	}

	//2. termination 1
	if (p == pattern.size()) {
		ret = (t == target.size());
		return ret;
	}

	//2. traverse
	if (pattern[p] == '*') {
		for (int skip=0;skip+t<=target.size();skip++){
			if(_wildcard(pattern,target,p+1,skip+t)) {
				ret = 1;
				return 1;
			}
		}
	}
	ret = 0;
	return 0;
}

vector<string> wildcard(string pattern,vector<string> target) {
	vector<string> ret;
	for (int i=0;i<target.size();i++) {
		memset(cache,-1,sizeof(cache));
		if (true == _wildcard(pattern,target[i], 0, 0)) {
			ret.push_back(target[i]);
		}
	}
	return ret;
}

int main() {
	int total=0;
	string input;
	getline(cin, input);
	sscanf( input.c_str(), "%d", &total);
	while (total--) {
		vector<string> tc_list;
		string pattern;
		string tc;
		int tc_count=0;
		getline(cin,pattern);
		getline(cin, input);
		sscanf( input.c_str(), "%d", &tc_count);
		tc_list.reserve(tc_count);
		while(tc_count--) {
			getline(cin,tc);
			tc_list.push_back(tc);
		}
		vector<string> ret = wildcard(pattern,tc_list);
		_print(ret);
	}
}

