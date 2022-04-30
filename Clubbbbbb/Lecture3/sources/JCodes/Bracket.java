public class Bracket {
    public static void main(String[] args) {
        String net = "(-,(/,(-,(-,2,4),6),7),(/,3.4,2.7))";
        System.out.println(getMidLength(net));
    }
    public static int getMidLength(String net){
        char[] subNet = net.substring(3, net.length()-1).toCharArray();// (/,(-,(-,2,4),6),7),(/,3.4,2.7)
        int stack = 0;
        int counter = 0;    
        if(subNet[0]!='('){
            while(subNet[counter]!=',') counter++;
            return counter;
        }
        for (counter = 0; counter < subNet.length; counter++) {
            if(subNet[counter]=='(') stack++;
            if(subNet[counter]==')') stack--;
            if(stack == 0) break;
        }
        return counter+1;
    }
}
