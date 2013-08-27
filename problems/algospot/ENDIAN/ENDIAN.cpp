#include <iostream>
#include <string>
#include <bitset>
using namespace std;

unsigned int endian(unsigned int inp) {
	bitset<32> bits(inp);
	bitset<32> rets(inp);
	int start = 24;
	for (size_t i=0;i<bits.size();i+=8){
		rets[start+0] = bits[i+0];
		rets[start+1] = bits[i+1];
		rets[start+2] = bits[i+2];
		rets[start+3] = bits[i+3];
		rets[start+4] = bits[i+4];
		rets[start+5] = bits[i+5];
		rets[start+6] = bits[i+6];
		rets[start+7] = bits[i+7];
		start-=8;
	}
	return rets.to_ulong();
}
int main() {
	unsigned int total=0;
	unsigned int det=0;
	unsigned int ret=0;
	string input;
	getline(cin, input);
	sscanf( input.c_str(), "%u", &total);
	while (total--) {
		getline(cin, input);
		sscanf( input.c_str(), "%u", &det);
		ret = endian(det);
		cout << ret << endl;
	}
}
