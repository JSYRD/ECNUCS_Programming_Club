public class IteratorTest {
    static void display(SeqIterator i){
        while(i.hasNext()) System.out.println(i.next().toString());
    }
    public static void main(String[] args) {
        ArraySequence arr = new ArraySequence(10);
        for(int i=0;i<10;i++){
            SequenceItem temp = new SequenceItem();
            temp.setData(Integer.toString(i));
            arr.add(temp);
        }
        IteratorTest i = new IteratorTest();
        i.display(arr.iterator());
    }
}
