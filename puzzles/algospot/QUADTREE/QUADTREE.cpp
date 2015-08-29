#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <cassert>
using namespace std;

string _reverse2(string::iterator& it) {
	//1. node-value get
	char head = *it;

	//2-1. basis
	if ('b' == head || 'w' == head) {
		return string(1, head);

	//2-2. traverse_with_next
	} else if ('x' == head) {
		string ul = _reverse2(++it);
		string ur = _reverse2(++it);
		string dl = _reverse2(++it);
		string dr = _reverse2(++it);
		return 'x'+dl+dr+ul+ur ;

	//2-3. exception
	} else {
		assert(0);
	}
}

string _reverse1(string::iterator& it) {
	//1. node-value get
	char head = *it;

	//2. next
	it++;

	//3-1. basis
	if ('b' == head || 'w' == head) {
		return string(1, head);

	//3-2. traverse
	} else if ('x' == head) {
		string ul = _reverse1(it);
		string ur = _reverse1(it);
		string dl = _reverse1(it);
		string dr = _reverse1(it);
		return 'x'+dl+dr+ul+ur ;

	//3-3. exception
	} else {
		assert(0);
	}
}

string quadtree(string input) {
	string::iterator it = input.begin();
	return _reverse(it);
}

int main() {
	int total=0;
	int casecount = 0;
	int ret = 0;
	string input;
	getline(cin, input);
	sscanf( input.c_str(), "%d", &total);
	while (total--) {
		string testcase;
		getline(cin,testcase);
		string ret = quadtree(testcase);
		cout << ret << endl;
	}
}

