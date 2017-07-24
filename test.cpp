#include "iostream"
#include "string.h"
#include "stdio.h"
#include <errno.h>
#define N 3
using namespace std;
struct student
{
	char num[6];
	int score;
	char key[15];
};
void menu()
{
	cout << "1.建立学生档案" << '\n' << "2.显示学生信息" << '\n' << "3.修改学生信息" << '\n' << "4.退出程序" << endl;
}
void create(student s[], int n)
{
	int i,j;
	student t;                 //注意：必须有student，否则不存在由student到int的转换
	cout << "请输入学生信息" << endl;
	for (i = 0; i < n; i++)
		cin >> s[i].num >> s[i].score >> s[i].key;
	for (i = 0; i < n-1;i++)
        for (j = 0; j < n - i-1;j++)
            if (s[j].score>s[j + 1].score)
            {
                t = s[j];
                s[j] = s[j + 1];
                s[j + 1] = t;
            }
}
void disp(student s[], int n)
{
	int i,j;
	for (i = 0; i < n; i++)
		cout << s[i].num <<'\t'<< s[i].score <<'\t';
	for (j = 0; s[i].key[j] != '\0'; j++)
		cout << "*";
	cout << endl;
}
void modify(student s[], int n)
{
	int i;
	char num[6];
	cout << "请输入要修改信息的学生学号： ";
		cin >> num;
		for (i = 0; i < n;i++)
		if (strcmp(num, s[i].num) == 0)
		{
			cout << "请输入要修改的学生成绩与密码：";
			cin >> s[i].score >> s[i].key;
			cout << endl;
			break;
		}
}
void quit(student s[], int n)
{
	FILE *fp;
	errno_t err;

    if ((err = fopen_s(&fp, "c:\\ks\\student.dat", "wb")) != 0) {
        cout << "can't open file\n" << endl;
		exit(1);
    } else {
        // File was opened, filepoint can be used to read the stream.
        fwrite(s, sizeof(s), 1, fp);
	    fclose(fp);
	    exit(1);
    }
}
int main()
{
	student s[N];
	int choice;
	while (1)
	{
		menu();
		cin >> choice;
		switch (choice)
		{
		case 1:create(s, N); break;
		case 2:disp(s, N); break;
		case 3:modify(s, N); break;
		case 4:quit(s, N); break;
		}
	}
	system("pause");
    return 0;
}