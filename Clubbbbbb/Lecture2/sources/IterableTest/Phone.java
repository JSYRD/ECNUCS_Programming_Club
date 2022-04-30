package IterableTest;
public class Phone{
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