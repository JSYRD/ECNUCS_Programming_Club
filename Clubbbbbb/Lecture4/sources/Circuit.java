public abstract class Circuit{
    char method;
    double resistance;
    double voltage;
    double electricy;
    Circuit resistor0;
    Circuit resistor1;
    public abstract double resistance();
    public Circuit(){

    }
    public static Circuit getCircuit(String net){
        if(net.length()==1) return new Single(net);
        if(net.charAt(1)=='-'){
            return new Series(net);
        }
        else if(net.charAt(1)=='/'){
            return new Parallel(net);
        }
        else{
            return new Single(net);
        }
    }
    public static int getMidLength(String net){
        char[] subNet = net.substring(3, net.length()-1).toCharArray();
        //   (/,(-,(-,2,4),6),7) , (/,3.4,2.7)
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
    public void setPower(double voltage){
        this.voltage = voltage;
        this.electricy = voltage/resistance;
        switch (this.method) {
            case '-':
                resistor0.setPower(electricy*resistor0.resistance);
                resistor1.setPower(electricy*resistor1.resistance);
            break;
            case '/':
                resistor0.setPower(voltage);
                resistor1.setPower(voltage);
            default:
                break;
        }
    }
    @Override
    public String toString() {
        if(this.method=='s') return String.valueOf(this.resistance);
        return String.format("(%c,%s,%s)", this.method,this.resistor0.toString(),this.resistor1.toString());
    }
}

class Parallel extends Circuit{
    public Parallel(String net) {
        this.method = '/';
        int midLength = getMidLength(net);
        this.resistor0 = Circuit.getCircuit(net.substring(3, 3+midLength));
        this.resistor1 = Circuit.getCircuit(net.substring(4+midLength,net.length()-1));
        this.resistance = 1/((1/resistor0.resistance)+(1/resistor1.resistance));
    }

    public double resistance(){
        return this.resistance;
    }
}

class Series extends Circuit{
    public Series(String net){
        this.method = '-';
        int midLength = getMidLength(net);
        this.resistor0 = Circuit.getCircuit(net.substring(3, 3+midLength));
        this.resistor1 = Circuit.getCircuit(net.substring(4+midLength,net.length()-1));
        this.resistance = this.resistor0.resistance+this.resistor1.resistance;
    }
    public double resistance(){
        return this.resistance;
    }
}

class Single extends Circuit{
    public Single(String net){
        this.method = 's';
        this.resistance = Double.parseDouble(net);
    }
    public double resistance(){
        return this.resistance;
    }
}

class TestCircuit{
    public static void main(String[] args) {
        // String net = "(-,(-,(-,3.5,(/,8.5,(/,1.8,(/,0.7,4.6)))),(/,(-,(/,(-,4.8,(/,2.4,6.3)),(-,3.7,(-,1.4,6.9))),3.8),(-,3.7,(/,(-,4.8,3.2),(-,3.7,4.4))))),(/,7.9,4.5))";
        String net = "(/,(-,3,3),(-,(/,6,3),2))";
        double voltage = 12.0;
        Circuit circuit = Circuit.getCircuit(net);
        circuit.setPower(voltage);
        System.out.println(circuit.toString());
        System.out.println(circuit.resistance());
    }
}