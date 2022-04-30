import java.util.*;

public class Foreach{
    public static void main(String[] args) {
        int []A = new int[10];
        for (int i = 0; i < A.length; i++) {
            A[i] = i;
        }
        List<Integer> B = new ArrayList<Integer>();
        for (int i = 0; i < 10; i++) {
            B.add(i);
        }
        Set<Integer> C = new HashSet<>();
        for (int i = 0; i < 10; i++) {
            C.add(i);
        }
        Map<Integer, String> D = new HashMap<Integer,String>();
        for (int i = 0; i < 10; i++) {
            D.put(i, String.valueOf(i));
        }
        //output
        for (int i = 0; i < A.length; i++) {
            System.out.print(A[i]);
        }
        System.out.println();
        for (int i : A) {
            System.out.print(i);
        }
        System.out.println();
        for (Integer i : B){
            System.out.print(i);
        }
        System.out.println();
        for (Integer i: C){
            System.out.print(i);
        }
        System.out.println();
        for (Map.Entry<Integer,String> i : D.entrySet()) {
            System.out.print(i.getValue());
        }
        System.out.println();
    }
}