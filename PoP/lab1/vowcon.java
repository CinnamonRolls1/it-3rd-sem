import java.util.Scanner;
import java.lang.*;
class vowcon{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter character");
		char ch = sc.next().charAt(0);
		char ch1 = Character.toLowerCase(ch);
		switch (ch1) {
		case 'a':
		case 'e':
		case 'i':
		case 'o':
		case 'u':
			System.out.println("Vowel");
			break;
		default:
			System.out.println("Consonant");
			break;
		}


		}
	}