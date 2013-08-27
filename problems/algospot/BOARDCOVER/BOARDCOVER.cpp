#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <cassert>
using namespace std;

#define TYPEMAX 4 //0-3
#define BLOCKMAX 3 //0-2

//{y,x}
const int blocktype[TYPEMAX][BLOCKMAX][2] = {
	{ {0,0}, {0,1}, {1,0} },
	{ {0,0}, {0,1}, {1,1} },
	{ {0,0}, {1,0}, {1,1} },
	{ {0,0}, {1,0}, {1,-1} }
};

int _print(vector<vector<int> >& board) {
	for(int i=0;i<board.size();i++) {
		for(int j=0;j<board[i].size();j++) {
			cout<<board[i][j]<<" ";
		}
		cout<<endl;
	}
	cout<<endl;
	return 1;
}

bool _set(vector<vector<int> >& board, int type, int y, int x, int delta) {
	bool ret = true;
	for (int i=0;i<BLOCKMAX;i++) {
		const int ny = y + blocktype[type][i][0];
		const int nx = x + blocktype[type][i][1];
		if (ny < 0 || nx < 0 || ny >= board.size() || nx >= board[0].size()) {
			ret = false;
		}
		else if ((board[ny][nx]+= delta) > 1) {
			ret = false;
		}
		if (0 > board[ny][nx]) {
			assert(0);
		}
	}
	return ret;
}

bool set(vector<vector<int> >& board, int type, int y, int x) {
	return _set(board,type,y,x,1);
}

bool unset(vector<vector<int> >& board, int type, int y, int x) {
	return _set(board,type,y,x,-1);
}

int _boardcover(vector<vector<int> >& board) {
	int y=-1;
	int x=-1;
	for(int i=0;i<board.size();i++) {
		for(int j=0;j<board[i].size();j++) {
			if (0 == board[i][j]) {
				y = i;
				x = j;
				goto target_find;
			}
		}
	}
	return 1;

	target_find:
	int ret = 0;
	for(int type=0;type<TYPEMAX;type++) {
		if (true == set(board, type, y, x) ){
			ret += _boardcover(board);
		}
		unset(board, type, y, x);
	}
	return ret;
}

int boardcover(vector<vector<int> >& board, int blank_len) {
	if (0 != blank_len%BLOCKMAX) {
		return 0;
	}
	return _boardcover(board);
}

int main() {
	int total=0;
	int w,h=0;
	int ret=0;
	string input;
	getline(cin, input);
	sscanf(input.c_str(), "%d", &total);
	while (total--) {
		getline(cin, input);
		sscanf(input.c_str(), "%d %d", &h, &w);
		vector<vector<int> > board;
		int blank_len=0;
		for (int i=0;i<h;i++) {
			vector<int> row;
			row.reserve(w);
			getline(cin, input);
			for (int j=0;j<w;j++) {
				if ('#' == input[j]) {
					row.push_back(1);
				} else if ('.' == input[j]) {
					row.push_back(0);
					blank_len++;
				} else {
					assert(0);
				}
			}
			board.push_back(row);
		}
		ret = boardcover(board,blank_len);
		cout << ret << endl;
		board.clear();
	}
}

