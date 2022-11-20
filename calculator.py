package psai1;
import java.util.Scanner;
public class new1 {
public static void main (String args[]) {
Scanner scan=new Scanner(System.in);
print("Welcome to RUTHVIK's calculator");
print("Instructions:1)please enter only integers while using !");
print("             2)please ensure that second number is integer while using ^");

print("enter first number");
double num1=scan.nextDouble();
print("select the operator + - * / sin cos tan sec cosec cot ! ^");
String s1=scan.next();
if (s1.equals("sin")) {
	print(""+sin(num1));
	
}
else if (s1.equals("cos")) {
	print(""+cos(num1));
	
}
else if (s1.equals("tan")) {
	print(""+tan(num1));
	
}
else if (s1.equals("sec")) {
	print(""+sec(num1));
	
}
else if (s1.equals("cosec")) {
	print(""+cosec(num1));
	
}
else if (s1.equals("cot")) {
	print(""+cot(num1));
	
}
else if (s1.equals("!")) {
	print(""+fac(num1));
	
}

else {
	print("enter second number");
	double num2=scan.nextDouble();
	if(s1.equals("+")) {
		System.out.println(num1+num2);
	}
	if(s1.equals("-")) {
		System.out.println(num1-num2);
	}
	if(s1.equals("*")) {
		System.out.println(num1*num2);
	}
	if(s1.equals("/")) {
		System.out.println(num1/num2);
	}
	if(s1.equals("^")) {
		System.out.println(pow(num1,num2));
	}
}

}

 static long fac (double a) {
	long c=1;
	for (int i=1;i<a+1;i++) {
		c=c*i;
	}
	return c;
 }
 static double pow(double a, double b) {
	 double c =1;
	 for(int i=0;i<b;i++) {
		c=c*a; 
	 }
	 return c;
 }
 static double sin(double a) {
	 double c=0;
	 for(int i=1;i<18;i++) {
		 c=c+pow(a,2*i-1)/fac(2*i-1)*pow(-1,i+1);
	 }
	 return c;
 }
 static void print (String a){
	System.out.println(a) ;
 }
 static double cos(double a) {
	 double c=1;
	 for(int i=1;i<10;i++) {
		 c=c+pow(a,2*i)/fac(2*i)*pow(-1,i);
	 }
	 return c;
 }
 static double tan(double a) {
	 return sin(a)/cos(a);
 }
 static double sec(double a) {
	 return 1/cos(a);
 }
 static double cosec(double a) {
	 return 1/sin(a);
 }
 static double cot(double a) {
	 return 1/tan(a);
 }
}
