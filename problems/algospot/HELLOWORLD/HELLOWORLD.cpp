#include <iostream>
char name[11];
main(int a){
	for(std::cin>>a;a;a--) {
		std::cin>>name;
		printf("Hello, %s!\n",name);
	}
}
