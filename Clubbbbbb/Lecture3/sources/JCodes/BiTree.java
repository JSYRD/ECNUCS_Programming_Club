import java.util.BitSet;

public class BiTree{
    int value;
    BiTree lchild;
    BiTree rchild;
    public BiTree(int value){
        this.value = value;
    }
}
class TestBiTree{
    public static void main(String[] args) {
        BiTree root = new BiTree(10);
        root.lchild = new BiTree(20);
        root.rchild = new BiTree(30);
        System.out.println("");
    }
}