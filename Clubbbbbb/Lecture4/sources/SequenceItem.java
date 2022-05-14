import java.util.Iterator;

public class SequenceItem {
    String data;
    String getData(){
        return data;
    }
    void setData(String data){
        this.data = data;
    }
    public String toString() {
        return data;
    }
    public boolean equals(SequenceItem item) {
        return this.data.equals(item.data);
    }
}

interface Sequence {
    void add(SequenceItem item);
    SequenceItem get(int i);
    void remove(SequenceItem item);
    boolean contains(SequenceItem item);
    int size();
    boolean isEmpty();

    SeqIterator iterator();
    SeqBiIterator reverseltIterator();
    SeqBiIterator biltIterator();


    SequenceItem [] toArray();
    boolean equals(ArraySequence seq);
    String toString();
}

interface SeqIterator extends Iterator{
    boolean hasNext();
    SequenceItem next();
    void remove();
}

interface SeqBiIterator extends SeqIterator,Iterator{
    boolean hasPrevious();
    SequenceItem previous();
}