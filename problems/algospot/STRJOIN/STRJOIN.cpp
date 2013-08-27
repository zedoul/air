#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
using namespace std;

int concat(const vector<int>& lengths) {
	priority_queue<int, vector<int>, greater<int> > pq;
	for (int i=0; i < lengths.size();++i) {
		pq.push(lengths[i]);
	}
	int ret = 0;
	while(pq.size() > 1) {
		int min1 = pq.top();pq.pop();
		int min2 = pq.top();pq.pop();
		pq.push(min1+min2);
		ret += min1 + min2;
	}
	return ret;
}

int strjoin(vector<int> tokens) {
	int cost = 0;
	int det1 = 0;
	int det2 = 0;
	while (tokens.size() > 1) {
		sort(tokens.begin(), tokens.end());
		det1 = *(tokens.begin());
		tokens.erase(tokens.begin());
		det2 = *(tokens.begin());
		tokens.erase(tokens.begin());
		cost += det1 + det2;
		tokens.push_back(det1 + det2);
	}
	return cost;
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
		ret = strjoin(tokens);
//		ret = concat(tokens);
		cout << ret << endl;
	}
}
