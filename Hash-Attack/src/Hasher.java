import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Hasher
{
    private MessageDigest digester;

    public Hasher()
    {
        try
        {
            digester = MessageDigest.getInstance("SHA-1");
        }
        catch (NoSuchAlgorithmException e)
        {
            e.printStackTrace();
        }
    }

    public JByte hash(String valueToHash, int bitLength)
    {
        JByte bitSet = new JByte(bitLength);
        byte[] hash = digester.digest(valueToHash.getBytes());
        int wordNum = 0;
        for (int i = 0; i < bitLength;)
        {
            String binaryString = Integer.toBinaryString(Math.abs(hash[wordNum]));
            wordNum++;
            for (int j = 0; j < binaryString.length(); j++)
            {
                if (binaryString.charAt(j) == '1')
                {
                    bitSet.set(i);
                }
                else
                {
                    bitSet.clear(i);
                }
                i++;
                if (i >= bitLength)
                    break;
            }
        }
        return bitSet;
    }
}
