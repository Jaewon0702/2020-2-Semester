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