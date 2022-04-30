package IterableTest;
import java.util.ArrayList;
import java.util.Iterator;

public class PhoneBox implements Iterable<Phone>{
    private ArrayList<Phone> box = new ArrayList<Phone>();
    public PhoneBox(){
        
    }
    public PhoneBox(Phone[] phones){
        for (Phone phone : phones) {
            box.add(phone);
        }
    }
    public boolean addPhone(Phone phone){
        return box.add(phone);
    }
    public boolean addPhone(Phone[] phones){
        boolean flag = true;
        for (Phone phone : phones) {
            if(!box.add(phone)){
                flag = false;
                break;
            }
        }
        return flag;
    }
    public boolean removePhone(Phone phone){
        return box.remove(phone);
    }
    @Override
    public Iterator<Phone> iterator() {
        return box.iterator();
    }    
}