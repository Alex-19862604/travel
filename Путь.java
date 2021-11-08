package Dec;
import java.util.Scanner; 
public class Secret {
 

	public static void main(String[] args) {
	System.out.println("Пожалуйста авторизуйтесь ");
		Scanner a = new Scanner(System.in);
		String s2= a.nextLine();
		System.out.println("Здравствуйте, " a );
		System.out.println("Выберите функцию [A продолжить маршрут] [J пропуск]");
		Scanner c = new Scanner(System.in);
		String s1= c.nextLine()
		if(s1.equalsIgnoreCase("A")) 
		
			System.out.println("Возвращаемся к предыдущему маршруту");
			//модуль возврата
			
			
			
			
			
			
			
		}else if(s1.equalsIgnoreCase("J")) {
			System.out.println("Выберите маршрут [1] [2] [3]");
			Scanner sc = new Scanner(System.in);
			String s3=sc.nextLine();
			if(s3.equalsIgnoreCase("1")) {
			System.out.println("Выбран маршрут 1");
			//модуль маршрута
			
			
			}else if(s3.equalsIgnoreCase("2")){
			System.out.println("Выбран маршрут 2");
			//модуль маршрута
			
			
			}else if(s3.equalsIgnoreCase("3")){
			System.out.println("Выбран маршрут 3");
			//модуль маршрута
			
			//и нужно как-то зациклить прогу на выборе функций,типа после окончания маршрута возврат к выбору
			