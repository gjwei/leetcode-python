#include "iostream"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#define N 20
using namespace std;
struct student
{
	char name[10];
	char num[7];
	char a[3];
};
void menu()
{
	cout << "1.建立学生档案" << '\t' << "2.显示学生信息" << '\t' << "3.查找指定学生信息" << endl;
	cout << "4.增加学生信息" << '\t' << "5.删除学生信息" << '\t' << "6.修改学生信息" << endl;
	cout << "7.统计各科最高分" << '\t' << "8.按学号排序" << '\t' << "9.保存学生信息" << endl;
	cout << "10.读入数组并退出程序" << endl;
}
void create(student s[], int n)
{
	int i ;
	cout << "请输入学生姓名，学号，英语成绩，数学成绩，语文成绩：" << endl;
	for (i = 0; i < n; i++)
		cin >> s[i].name >> s[i].num >> s[i].a[0] >> s[i].a[1] >> s[i].a[2];
}
void display(student s[], int n)
{
	int i;
	for (i = 0; i < n; i++)
	{
		cout << "学生姓名：" << s[i].name << endl;
		cout << "学生学号：" << s[i].num << endl;
		cout << "英语成绩：" << s[i].a[0] << endl;
		cout << "数学成绩：" << s[i].a[1] << endl;
		cout << "语文成绩：" << s[i].a[2] << endl;
	}
}
void search(student s[], int n)
{
	int i;
	char xuehao[7];
	cout << "请输入学生学号或姓名" << endl;
	cin >> xuehao;
	for (i = 0; i < n; i++)
	{
		if (strcmp(xuehao, s[i].num) == 0)
			break;
	}
	if (i < n)
	{
		cout << "学生姓名：" << s[i].name << endl;
		cout << "学生学号：" << s[i].num << endl;
		cout << "英语成绩：" << s[i].a[0] << endl;
		cout << "数学成绩：" << s[i].a[1] << endl;
		cout << "语文成绩：" << s[i].a[2] << endl;
	}
	if (i == n)
		cout << "查找不到学生记录" << endl;
}
int append(student s[], int n)
{
	int yingyu,shuxue,yuwen;
	char xuehao[7], xingming[10];
	cout << "请输入要添加学生的信息" << endl;
	cin >> xingming>> xuehao >> yingyu >> shuxue >> yuwen;
	student *p = s;
	p = p + n;
	strcpy(p->name, xingming);
	strcpy(p->num, xuehao);
	p->a[0] = yingyu; p->a[1] = shuxue; p->a[2] = yuwen;
	return n + 1;
}
int del(student s[], int n)
{
	int i;
	char xuehao[7];
	cout << "请输入要删除学生的学号" << endl;
	cin >> xuehao;
	for (i = 0; i < n; i++)
	{
		if (strcmp(xuehao, s[i].name) == 0)
			break;
	}
	for (i = 0; i < n - 1; i++)
	{
		s[i] = s[i + 1];
	}
	return n - 1;
}
void modify(student s[], int n)
{
	int i,yingyu,shuxue,yuwen;
	char xingming[10],xuehao[7];
	cout << "请输入被修改信息学生的姓名:" << endl;
	cin >> xingming>>xuehao>>yingyu>>shuxue>>yuwen;
	for (i = 0; i < n; i++)
	{
		if (strcmp(xingming, s[i].name) == 0)
			break;
	}
	if (i == n)
		cout << "未找到学生记录" << endl;
	else
	{
		strcpy(s[i].name, xingming);
		s[i].a[0] = yingyu;
		s[i].a[1] = shuxue;
		s[i].a[2] = yuwen;
	}
}
void count(student s[], int n)
{
	int max1, max2, max3,i;
	max1 = s[0].a[0];
	max2 = s[0].a[1];
	max3 = s[0].a[2];
	for (i = 1; i < n; i++)
	{
		if (max1 < s[i].a[0])
			max1 = s[i].a[0];
		if (max2 < s[i].a[1])
			max2 = s[i].a[1];
		if (max3 < s[i].a[2])
			max3 = s[i].a[2];
	}
	cout << "英语最高分：" << max1 << '\n' << "数学最高分" << max2 << '\n' << "语文最高分" << max3 << endl;
}
void sort(student s[], int n)
{
	int i,j;
	student t;
	for (i = 1; i < n; i++)
	{
		for (j = 0; i < n - 1;j++)
		if (s[j].num>s[j + 1].num)
		{
			t = s[j];
			s[j] = s[j + 1];
			s[j + 1] = t;
		}
	}
}
void save(student s[], int n)
{
	FILE *fp;
	fp = fopen("data", "wb");
	if (fp == NULL)
	{
		cout << "can't open file\n" << endl;
		exit(1);
	}
	fwrite(s, sizeof(s), n, fp);
	fclose(fp);
}
void readfile(student s[], int n)
{
	FILE *fp;
	fp = fopen("c:\\ks\\student.dat", "rb");
	if (fp == NULL)
	{
		cout << "can't open file\n" << endl;
		exit(1);
	}
	fread(s, sizeof(s), n, fp);
	fclose(fp);
	exit(1);
}
int main()
{
	int choice;
	student s[N];
	while (1)
	{
		menu();
		cin >> choice;
		switch (choice)
		{
		case 1:create(s, N); break;
		case 2:display(s, N); break;
		case 3:search(s, N); break;
		case 4: append(s, N); break;
		case 5:del(s, N); break;
		case 6:modify(s, N); break;
		case 7:count(s, N); break;
		case 8:sort(s, N); break;
		case 9:save(s, N); break;
		case 10:readfile(s, N); break;
		}
	}
	system("pause");
    return 0;
}
