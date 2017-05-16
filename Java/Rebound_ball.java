package Practice;
/*
 * 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在 第10次落地时，共经过多少米？第10次反弹多高？
 */
import java.util.Scanner;
public class Rebound_ball {
	public static void main(String[] args){
		System.out.print("请输入小球落地时的高度和求解的次数：");
		Scanner scan = new Scanner(System.in).useDelimiter("\\s");
		int h = scan.nextInt();
		int n = scan.nextInt();
		scan.close();
		distance(h,n);
	}
	//小球从h高度落下，经n次反弹后经过的距离和反弹的高度
	private static void distance(int h,int n){
		double length = 0;
		for(int i=0;i<n;i++){
			length += h;
			h /=2.0 ;
		}
		System.out.println("经过第"+n+"次反弹后，小球共经过"+length+"米，"+"第"+n+"次反弹高度为"+h+"米");
	}

}
