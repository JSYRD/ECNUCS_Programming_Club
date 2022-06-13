public class Test{
    public static void main(String[] args){
        // ClassA a = new ClassA();
        ClassB b = new ClassB();
    }
}
class ClassA{
    int a = 1;
    public ClassA(){
        methodA();
    }
    public void methodA(){
        System.out.println("ClassA.methodA");
    }
}
class ClassB extends ClassA{
    int a = 2;
    public ClassB(){
        methodA();
    }
    @Override
    public void methodA(){
        System.out.println("ClassB.methodA");
    }
}