public class Animal {
    String name;
    public Animal(){

    }
    public Animal(String name){
        this.name = name;
    }
    void eat(){
        System.out.println("Animal eating.");
    }
    public static void main(String[] args) {
        Cat cat0 = new Cat("meow");

        Animal cat1 = new Cat("meow");

        Animal animal = new Animal("I don't know");

        cat0.eat();

        cat1.eat();

        animal.eat();
    }
}
class Cat extends Animal{
    public Cat(){
        super();
    }
    public Cat(String name){
        super(name);
    }
    
    @Override
    void eat(){
        System.out.println("Cat eating.");
    }
}
