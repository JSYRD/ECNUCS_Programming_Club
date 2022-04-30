public class WrappedClassCache {
    public static void main(String[] args) {
        Integer.valueOf(8);
        Integer b = 8;
        // System.out.println(a==b);

        Integer c = 128;
        Integer d = 128;
        System.out.println(c==d);
    }
}
