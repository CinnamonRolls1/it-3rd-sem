import java.util.Scanner;
class arrcalc{
	public static void main (String[] args){
	Scanner sc = new Scanner(System.in);
	System.out.println("Enter no of columns:");
	int n = sc.nextInt();
	System.out.println("Enter no of rows:");
	int m = sc.nextInt();
	int arr[][];
	arr = new int[n][m];
	System.out.println("Enter values of first matrix:");
	for (int i = 0; i < n; i++){
		System.out.println("Row no"+(i+1));
		for (int j = 0; j < m; j++){
			arr[i][j] = sc.nextInt();
			}	
		}
	int arr2[][];
	arr2 = new int[n][m];
	System.out.println("Enter values of second matrix:");
	for (int i = 0; i < n; i++){
		System.out.println("Row no"+(i+1));
		for (int j = 0; j < m; j++){
			arr2[i][j] = sc.nextInt();
			}	
		}

	System.out.println("Sum:");
	for (int i = 0; i < n; i++){
		for (int j = 0; j < m; j++){
			System.out.print((arr[i][j]+arr2[i][j]+" "));
			}	
		System.out.println();
		}

	System.out.println("Difference:");
	for (int i = 0; i < n; i++){
		for (int j = 0; j < m; j++){
			System.out.print((arr[i][j]-arr2[i][j]+" "));
			}	
		System.out.println();
		}

	int tarr[][];
	tarr = new int[m][n];
	for (int i = 0; i < n; i++){
		for (int j = 0; j < m; j++){
			tarr[j][i]=arr[i][j];
			}	
		}

	System.out.println("Transpose of first matrix:");
	for (int i = 0; i < m; i++){
		for (int j = 0; j < n; j++){
			System.out.print(tarr[i][j]+" ");
			}	
		System.out.println();
		}

	int tarr2[][];
	tarr2 = new int[m][n];
	for (int i = 0; i < n; i++){
		for (int j = 0; j < m; j++){
			tarr2[j][i]=arr2[i][j];
			}	
		}

	System.out.println("Transpose of second matrix:");
	for (int i = 0; i < m; i++){
		for (int j = 0; j < n; j++){
			System.out.print(tarr2[i][j]+" ");
			}	
		System.out.println();
		}

	System.out.println("Enter value to search in first matrix:");
	int ch = sc.nextInt();
	int f = 0;
	for (int i = 0; i < n; i++){
		for (int j = 0; j < m; j++){
			if(arr[i][j]==ch){
				System.out.println("Found at "+(i+1)+","+(j+1));
				f=1;	
			} 
			}	
		}
	if(f==0){
		System.out.println("Value not found");
	}

	}
}