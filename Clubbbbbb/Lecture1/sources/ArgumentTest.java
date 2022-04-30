public class ArgumentTest {
    static void arrayAddOne(int b[]) {
        for (int i = 0; i < b.length; ++i)
            b[i]++;
    }

    static void intAddOne(int y) {
        y++;
    }

    public static void main(String[] args) {
        final int x = 0;
        ArgumentTest.intAddOne(x);
        final int[] a = { 1, 2, 3, 4, 5 };
        ArgumentTest.arrayAddOne(a);
    }
}