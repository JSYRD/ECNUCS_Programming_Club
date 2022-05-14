public class ArraySequence implements Sequence{
    private SequenceItem item[];
    private int size;
    private int next=0;
    public ArraySequence(int size){
        this.size = size;
        this.item = new SequenceItem[size];
    }
    private void bigger(){
        SequenceItem []temp = (SequenceItem[])this.item.clone();
        this.size = this.size*2;
        this.item = new SequenceItem[this.size];
        for (int i = 0; i < temp.length; i++) {
            this.item[i]=temp[i];
        }
    }
    private void smaller(){
        SequenceItem []temp = (SequenceItem[])this.item.clone();
        this.size = this.size/2;
        this.item = new SequenceItem[this.size];
        for (int i = 0; i < temp.length; i++) {
            this.item[i]=temp[i];
        }
    }
    public void add(SequenceItem item){
        if(next==this.size) bigger();
        this.item[next++]=item;
    }
    public SequenceItem get(int i){
        return this.item[i];
    }
    public void remove(SequenceItem item){
        for(int i=0;i<size&&(this.item[i]!=null);i++){
            if(this.item[i].equals(item)){
                next--;
                SequenceItem []temp = new SequenceItem[size];
                for(int j=0,t=0;j<size&&(this.item[j]!=null);j++,t++){
                    if(j==i) continue;
                    else temp[t]=this.item[j];
                }
                this.item=temp;
            }
        }
        if(next<size/4) smaller();
    }
    public SeqIterator iterator(){
        return new SequenceIterator();
    }
    public SeqBiIterator reverseltIterator(){
        return new SequenceBiIterator();
    }
    public SeqBiIterator biltIterator(){
        return new SequenceBiIterator();
    }

    private class SequenceIterator implements SeqIterator{
        private int i=0;
        public boolean hasNext(){
            return i<item.length&&item[i]!=null;
        }
        public SequenceItem next(){
            return item[i++];
        }
        public void remove(){

        }
    }
    private class SequenceBiIterator implements SeqBiIterator{
        private int i=0;
        public boolean hasNext(){
            return item[i]!=null;
        }
        public SequenceItem next(){
            return item[i++];
        }
        public void remove(){

        }
        public boolean hasPrevious(){
            return (i>0)&&(item[i-1]!=null);
        }
        public SequenceItem previous(){
            return item[--i];
        }
    }
    public boolean contains(SequenceItem item){
        for(int i=0;i<size&&(this.item[i]!=null);i++){
            if(this.item[i].equals(item)) return true;
        }
        return false;
    }
    public int size(){
        return size;
    }
    public boolean isEmpty(){
        return item[0]==null;
    }
    public SequenceItem [] toArray(){
        return this.item;
    }
    public boolean equals(ArraySequence seq){
        if(this.item.length!=seq.item.length) return false;
        else{
            for(int i=0;(i<this.item.length)&&(item[i]!=null)&&(seq.item[i]!=null);i++){
                if(!item[i].equals(seq.item[i])) return false;
            }
            return true;
        }
    }
    @Override
    public String toString(){
        String temp ="";
        for(int i=0;i<size&&(this.item[i]!=null);i++) {
            temp+=this.item[i].toString()+",";
        }
        return "["+temp+"]";
    }
    public static void main(String[] args) {
        ArraySequence arr = new ArraySequence(10);
        for(int i=0;i<10;i++){
            SequenceItem temp = new SequenceItem();
            temp.setData(Integer.toString(i));
            arr.add(temp);
        }
        ArraySequence arr2 = new ArraySequence(4);
        for(int i=0;i<10;i++){
            SequenceItem temp = new SequenceItem();
            temp.setData(Integer.toString(i));
            arr2.add(temp);
        }
        SequenceItem a = new SequenceItem();
        a.setData("9");
        arr.add(a);
        System.out.println(arr);
        arr.remove(a);
        System.out.println(arr);
    }
}


