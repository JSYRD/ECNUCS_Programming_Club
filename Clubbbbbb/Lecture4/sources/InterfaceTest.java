import java.util.ArrayList;
import java.util.Iterator;

public class InterfaceTest{
    public static void main(String[] args) {
        ArrayList<Integer> arrayList = new ArrayList<>();
        for(int i=0;i<10;++i){
            arrayList.add(i);
        }
        Iterator arrayIterator = arrayList.iterator();
        while(arrayIterator.hasNext()){
            Integer integer = (Integer)arrayIterator.next();
            System.out.println(integer);
        }
    }
}
interface Cat{
    public void say();
}
interface Dog{
    public void say();
}

class Cog implements Cat, Dog{
    @Override
    public void say(){
        System.out.println("Woow");
    }
}
