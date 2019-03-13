import java.util.Scanner;
class studeet{
	public class Student{
		private int marks;
		private int fund;
		private int id;

	public Student(int marks, int fund, int id){
		this.marks = marks;
		this.fund = fund;
		this.id = id;
	}
	public int getmarks() {
		return this.marks;
	} 
	
	public int getfund() {
		return this.fund;
	} 

	public int getid() {
		return this.id;
	} 

	}
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter number of students:");
		int n = sc.nextInt();
		Student[] stud = new Student[n];
		for(int i = 0; i < n; i++){
			System.out.println("Enter marks, funds and ID of student "+(i+1));
			
			stud[i].marks = sc.nextInt();
			stud[i].fund = sc.nextInt();
			stud[i].id = sc.nextInt();
		}
		System.out.println("Search by ID:");
		int val = sc.nextInt();
		int f= 0;
		for(int i = 0; i < n; i++){
			if(stud[i].id == val){
				System.out.println("Found!");
				int fu=stud[i].getfund();
				int ma=stud[i].getmarks();
				System.out.println("Funds="+fu+" Marks="+ma);
				f=1;
			}
		}
		if(f==0){
			System.out.println("Student not found");
		}
	}	
}