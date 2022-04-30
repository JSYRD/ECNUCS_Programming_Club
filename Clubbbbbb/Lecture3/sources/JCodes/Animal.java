public abstract class Animal {
    int weight;
    public abstract void eat();
}
class Human extends Animal{
    public void eat(){
        System.out.println("Human eats.");
    }
    public static void main(String[] args) {
        Animal human = new Human();
        human.eat();
    }
}
