import java.math.BigInteger;
import java.security.SecureRandom;
import java.util.HashSet;
import java.util.Set;

public class Main
{
    private static int BIT_LENGTH = 16;
    private static Hasher hasher = new Hasher();
    private static SecureRandom random = new SecureRandom();

    public static void main(String[] args)
    {
        Set<String> data = new HashSet<>();
        String startingBirthday = generateHash();
        data.add(startingBirthday);
//        boolean noMatch = true;
        int iterations =  0;
        int collisions = 0;
        while (true)
        {
            iterations++;
            String hash = generateHash();
            if (!data.add(hash))
            {
                collisions++;
            }
            if (hash.equals(startingBirthday))
            {
                break;
            }
        }
        System.out.println("Completed after " + iterations + " iterations and " + collisions + " collisions");
    }

    private static String generateHash()
    {
        JByte bitSet = hasher.hash(new BigInteger(130, random).toString(32), BIT_LENGTH);
        return bitSet.toString();
    }
}
