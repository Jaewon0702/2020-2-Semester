/*
#include <stdio.h>
int main(){
	// 변수선언
	char name[10]; //이름
	char gender ; //성별(M, F)
	int eng, math, com; //영어, 수학, 컴퓨터
	double avg, GPA ; // 평균, 평점

	//자료입력
	printf("이름?");
	//scanf("%s", name);
	//fflush(stdin);
	gets(name);
	printf("성별(남자 M, 여자 F)?");
	gender = getchar();
    printf("영어 수학 컴퓨터 점수?");
	scanf("%d %d %d", &eng, &math, &com);
    
	//자료처리
	avg= (eng + math + com)/3.0;
	GPA = (avg * 4.5)/100;

	//결과출력
	printf("================\n");
	printf("이름 성별: %s %c", name, gender );
	printf("------------------\n");
	printf("%-6s : %3d점 \n", "영어", eng);
	printf("%-6s : %3d점 \n", "수학", math);
	printf("%-6s : %3d점 \n", "컴퓨터", com);
	printf("------------------\n");
	printf("평균(평점): %.2lf점 (%.2lf)\n", avg, GPA);
	printf("================\n");




	return 0;
} 
*/
// C++
#include <iostream>
using namespace std;
int main(){
	// 변수선언
	char name[10]; //이름
	char gender ; //성별(M, F)
	int eng, math, com; //영어, 수학, 컴퓨터
	double avg, GPA ; // 평균, 평점

	//자료입력
	cout <<"이름?";
	//cin>>name;
	cin.getline(name, 10)
	cout<<"성별(남자 M, 여자 F)?";
	cin >> gender;

    cout<< "영어 수학 컴퓨터 점수?";
	cin >> eng >> math >> com;

    
	//자료처리
	avg= (eng + math + com)/3.0;
	GPA = (avg * 4.5)/100;

	//결과출력
	cout << "================\n";
	cout <<"이름 (성별):" << name << "(" << gender << ")\n";
    cout <<"------------------\n";
	cout << "영어 :" << "eng" << "\n";
	cout << "수학 :" << "" << "\n";
	cout << "영어 :" << "eng" << "\n";


	printf("------------------\n");
	printf("평균(평점): %.2lf점 (%.2lf)\n", avg, GPA);
	printf("================\n");




	return 0;
}