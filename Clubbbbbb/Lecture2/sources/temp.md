举个例子
=====

* **Java源代码如下：**

```java
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
class Phone{
    private int id;
    private String brand;
    public Phone(int id, String brand){
        this.id = id;
        this.brand = brand;
    }
    
    public void setId(int id) {
        this.id = id;
    }
    public void setBrand(String brand) {
        this.brand = brand;
    }
    public String getBrand() {
        return brand;
    }
    public int getId() {
        return id;
    }//getter & setter
}
```

$$
E = mc^2
$$

