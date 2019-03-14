import java.util.Scanner;
class counter{
    public static void main (String[] args){
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter string:");
    String s = sc.nextLine();
    int count = 0;

    for (int i = 0; i < s.length(); i++) {
        if (s.charAt(i) == ' ') {
            System.out.println("count is " + count);
            count = 0;
        } else {
            count++;
        }
        }
    System.out.println("count is " + count);
    }   
}