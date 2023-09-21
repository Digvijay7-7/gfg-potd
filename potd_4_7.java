/* 
class potd_4_7{
    public static void main(String[] args) {
        int n = 4;
        int k = 10;
        int a[] = {1, 2, 3, 4};
        int c = 0, d = 0;
        int i;

        for(i = 0; i<n; i++){
            if (a[i]< k){
                c++;
            }
            if () ){
                d++;
            }
        }
        System.out.println(c);
        System.out.println(d);
    }
}
*/

/**
 * potd_4_7
 */
public class potd_4_7 {

    public static void main(String[] args) {
        int c = 0, N = 12345;
        while (N !=0) {
            N /=10;
            ++c;  
        }
        System.out.println(c);
    }
} 