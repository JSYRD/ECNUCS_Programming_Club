package IterableTest;
public class IteratorTest {
    public static void main(String[] args) {
        PhoneBox phoneBox = new PhoneBox();
        PhoneBoxUsingList phoneBoxUsingList = new PhoneBoxUsingList(10);
        for(int i=0;i<10;i++){
            Phone iPhone = new Phone(i, "Apple");
            Phone WHPhone = new Phone(i+10,"HUAWEI");
            phoneBox.addPhone(iPhone);
            phoneBoxUsingList.addPhone(WHPhone);
        }
    }
}