import java.math.BigInteger;

public class SrinivasNumber {

    // Function to compute (n permute k)
    public static BigInteger nPk(int n, int k) {
        BigInteger result = BigInteger.ONE;
        for (int x = n - k + 1; x <= n; x++)
            result = result.multiply(BigInteger.valueOf(x));
        return result;
    }

    // Function to compute the optimized Srinivas number
    public static BigInteger optimizedSrinivasNumber(int[] a) {
        int[] s = { 3, 2, 1, 2, 3, 1, 1, 1 };
        BigInteger result = BigInteger.valueOf(1);
        for (int i = 0; i < a.length; i++)
            result = result.multiply(nPk(a[i], s[i]));
        return result;
    }

    public static void main(String[] args) {
        int N = 100;
        int[] counts = { 4, 2, 3, 2, 4, 2, 2, 2 };
        for (int i = 0; i < counts.length; i++)
            counts[i] *= N;
        long start = System.currentTimeMillis();
        BigInteger result = optimizedSrinivasNumber(counts);
        System.out.println("TIME TAKEN: "+(System.currentTimeMillis() - start) / 1000000.0);
        System.out.println(result);
    }
}
