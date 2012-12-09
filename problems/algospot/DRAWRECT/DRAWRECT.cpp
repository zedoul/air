#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;
vector<int> drawrect(vector<int> vx,vector<int> vy){
	vector<int> ret;
	map<int,int> mx,my;
	vector<int>::iterator it;
	for (it=vx.begin();it!=vx.end();it++){
		mx[(*it)]++;
	}
	for (it=vy.begin();it!=vy.end();it++){
		my[(*it)]++;
	}
	map<int,int>::iterator mit;
	for (mit=mx.begin();mit!=mx.end();mit++){
		if ((*mit).second == 1){
			ret.push_back((*mit).first);
			break;
		}
	}
	for (mit=my.begin();mit!=my.end();mit++){
		if ((*mit).second == 1){
			ret.push_back((*mit).first);
			break;
		}
	}
	return ret;
}

main() {
	int total=0;
	int count=3;
	string input;
	getline(cin, input);
	sscanf( input.c_str(), "%d", &total);
	while (total--) {
		vector<int> vx,vy;
		while(count--) {
			int x,y;
			getline(cin,input);
			sscanf(input.c_str(),"%d %d",&x,&y);
			vx.push_back(x);
			vy.push_back(y);
		}
		vector<int> det = drawrect(vx,vy);
		cout << det[0] << " " << det[1] << endl;
		count = 3;
	}
}
