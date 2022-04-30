import java.util.*;

public class Test {
    public static void main(String[] args) {
        List<Integer> intList = new ArrayList<>();
        ArrayList<Item> itemList = new ArrayList<>();
        itemList.add(new Item(10, 1.0, 'a'));
        itemList.add(new Item(11, 1.1, 'b'));
        ArrayList<Item> items = (ArrayList<Item>) itemList.clone();
        for (Item item : items) {
            System.out.println(item.i);
        }
    }
}
class Item{
    int i;
    double d;
    char c;
    public Item(int i,double d, char c){
        this.i = i;
        this.d = d;
        this.c = c;
    }
}