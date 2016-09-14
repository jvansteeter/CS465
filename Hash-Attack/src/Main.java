import java.math.BigInteger;
import java.security.SecureRandom;
import java.util.HashSet;
import java.util.Set;

public class Main
{
    public static void main(String[] args)
    {
        Hasher hasher = new Hasher();
        SecureRandom random = new SecureRandom();
        Set<String> data = new HashSet<>();
        boolean noMatch = true;
        int iterations =  0;
        while (noMatch)
        {
            JByte bitSet = hasher.hash(new BigInteger(130, random).toString(32), 64);
//            BitSet bitSet = hasher.hash("test", 16);
//            System.out.println(bitSet.toString());
            noMatch = data.add(bitSet.toString());
            iterations++;
        }
        System.out.println("Completed after " + iterations + " iterations");
    }
}
