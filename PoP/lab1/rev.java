import java.util.Scanner;
class rev{
	public static void main (String[] args){
	Scanner sc = new Scanner(System.in);
	System.out.println("Enter length:");
	int n = sc.nextInt();
	int arr[];
	arr = new int[n];
	System.out.println("Enter values:");
	for (int i = 0; i < n; i++){
		arr[i] = sc.nextInt();
	}
	System.out.println("Reversed:");
	for (int p = 0; p < n; p++){
			System.out.println(arr[n-p-1]);
		}
	}
}