public class FactoryTest{

}

class ShapeFactory{
    public static Shape getShape(String ShapeType){
        if(ShapeType == null){
            return null;
        }
        if(ShapeType.equalsIgnoreCase("RECTANGLE")){
            return new Rectangle();
        }
        else if(ShapeType.equalsIgnoreCase("Square")){
            return new Square();
        }
        else if(ShapeType.equalsIgnoreCase("Circle")){
            return new Circle();
        }
        return null;
}

interface Shape{
    void draw();
}
class Rectangle implements Shape{
    protected Rectangle(){}
    @Override
    public void draw(){
        System.out.println("Draw Rectangle");
    };
}
class Square implements Shape{
    protected Square(){}
    @Override
    public void draw(){
        System.out.println("Draw Square");
    };
}
class Circle implements Shape{
    protected Circle(){}
    @Override
    public void draw(){
        System.out.println("Draw Circle");
    };
}