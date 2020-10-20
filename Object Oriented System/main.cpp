//구구단 출력하기
#include <iostream>
#include <iomanip>
using namespace std;
int main(){
	int dan, i;
	/*cout <<"출력을 원하는 단은?";
	cin>>dan;
	for(i=1;i<=9;i++)
		cout<<dan<<"*"<<i<<"="<<dan*i<<"\n";*/
	for(dan=1;dan<=9;dan++){
		for(i=1;i<=9;i++)
			cout<<dan<<"*"<<i<<"="<<setw(2)<<dan*i<<"\t";
		cout<<"\n";

	}


}