
#include <iostream>
using namespace std;

class Student{
    public:
    string n;
    string b;
    int a;


    Student(string name,string branch,int age){
    n=name;
    b=branch;
    a=age;
    }
    void intro(){
    cout<<"HI guys,myself  "<<n<<"i am in "<<b<<"branch "<<"I am "<<a<<" years old"<<endl;
    }
};
int main()
{
 Student stud1("Pradeep","cs",50);
stud1.intro();
return 0;
}