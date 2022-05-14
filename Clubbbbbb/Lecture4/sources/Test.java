import java.util.ArrayList;
import java.util.Iterator;

public class Test{
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(114514);
        Iterator iterator = list.iterator();
        
        list.add(1919810);
        System.out.println(iterator.next());
    }
}