import java.util.Scanner;
class calc{
	public static void main (String[] args){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter a:");
		double a = sc.nextDouble();
		System.out.println("Enter b:");
		double b = sc.nextDouble();
		System.out.println("Enter operator:");
		char ch = sc.next().charAt(0);
		switch (ch) {
		case '+':
			System.out.println(a+b);
			break;
		case '-':
			System.out.println(a-b);
			break;
		case '/':
			System.out.println(a/b);
			break;
		case '*':
			System.out.println(a*b);
			break;
		default:
			System.out.println("Invalid input");
			break;
		}

	}
}