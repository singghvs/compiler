class Factorial{
    public static void main(String[] a){
        System.out.println(10);
    }
}
class Exemplo1{
    public boolean metodoA(int a){
        System.out.println(new B().metodoB(10));
        return true;
    }
}

class B {
    public int metodoB(int value) {
        return value * 2;
    }
}
class Exemplo2{
    public int metodoC(int a){
        int[] myIntArray;
        myIntArray = new int[100];
        System.out.println(myIntArray.length);
        if(a < 10){
            System.out.println(10);
        }
        else{
            System.out.println(100);
        }
        return a ;
    }
}