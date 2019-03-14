import java.util.Scanner;
class strcopy{
	public static void main (String[] args){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter string");
		String s = sc.nextLine();
		String copy = "";
		for (int i = 0; i < s.length(); i++){
			copy = copy + s.charAt(i);
		}
		System.out.println("Copied string:\n" + copy);


	}
}