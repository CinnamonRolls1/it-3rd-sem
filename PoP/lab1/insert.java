import java.util.Scanner;
class insert {
	public static void main(String a[]){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter length:");
		int n = sc.nextInt();
		int arr[];
		arr = new int[n];
		System.out.println("Enter values:");
		for (int i = 0; i < n; i++){
			arr[i] = sc.nextInt();
		}
		for (int k = 1; k < n; k++){
			int key = arr[k];
			int j = k-1;
			while ((j>-1) && (arr[j]>key)){
				arr[j+1]=arr[j];
				j--;

			}
			arr[j+1]=key;

		}
		System.out.println("Sorted:");
		for (int p = 0; p < n; p++){
			System.out.println(arr[p]);
		}
	}
}