import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		try (
			Scanner	scanner = new Scanner(System.in)){
			long a = scanner.nextLong();
			long b = scanner.nextLong();
			
			long total = a-b;
			
			if(total < 0) {
				total *= -1;
			}
			
			System.out.println(total);
		}
		
	}
}
