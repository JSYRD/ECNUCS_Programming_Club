package IterableTest;
import java.util.Iterator;

public class PhoneBoxUsingList implements Iterable<Phone>{
    private Phone[] box;
    public PhoneBoxUsingList(int max){
        box = new Phone[max];
    }
    public PhoneBoxUsingList(Phone[] phones, int max){
        box = new Phone[max];
        int i=0;
        for (Phone phone : phones) {
            box[i++] = phone;
        }
    }

    public boolean addPhone(Phone phone){
        for(int i=0;i<box.length;i++){
            if(box[i]==null){
                box[i] = phone;
                return true;
            }
        }
        return false;
    }

    public boolean addPhone(Phone[] phones){
        boolean flag = true;
        for (Phone phone : phones) {
            if(!addPhone(phone)){
                flag = false;
                break;
            }
        }
        return flag;
    }

    private class BoxIterator implements Iterator<Phone>{
        int index = 0;
        public boolean hasNext(){
            if(index<box.length && box[index+1]!=null) return true;
            return false;
        }
        public Phone next(){
            return box[++index];
        }
    }
    @Override
    public Iterator<Phone> iterator() {
        return new BoxIterator();
    }    
}