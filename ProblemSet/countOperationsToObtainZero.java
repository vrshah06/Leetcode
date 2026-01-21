class Count {
    public int countOperations(int num1, int num2) {
        int count = 0;
        while (num1 != 0 && num2 != 0) {
            if (num1 >= num2) {
                num1 -= num2;
            } else {
                num2 -= num1;
            }
            count++;
        }
        return count;
    }
}

class countOperationsToObtainZero {
    public static void main(String args[]) {
        Count obj = new Count();
        int num1 = 2, num2 = 3;
        int result = obj.countOperations(num1, num2);
        System.out.println("Number of operations to obtain zero: " + result);
    }
}
