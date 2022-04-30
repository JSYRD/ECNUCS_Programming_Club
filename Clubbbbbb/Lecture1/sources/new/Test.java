public class Test {
    int i;
    char c;
    String s;
    static int t;

    public Test(int i, char c, String s) {
        this.i = i;
        this.c = c;
        this.s = s;
    }

    public void setC(char c) {
        this.c = c;
    }

    public void setI(int i) {
        this.i = i;
    }

    public void setS(String s) {
        this.s = s;
    }

    public static void setT(int t) {
        Test.t = t;
    }
    @Override
    public boolean equals(Object obj) {
        // TODO Auto-generated method stub
        return ((Test)obj).i==this.i;
    }
}

class Run {
    public static void main(String[] args) {
        Test a = new Test(0, 'a', "123");
        Test b = new Test(0, 'a', "123");
        System.out.println(a.equals(b));
    }
}