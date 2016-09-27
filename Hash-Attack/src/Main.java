import java.io.*;
import java.math.BigInteger;
import java.security.SecureRandom;
import java.util.HashSet;
import java.util.Set;

public class Main
{
    private static int BIT_LENGTH = 1;
    private static Hasher hasher = new Hasher();
    private static SecureRandom random = new SecureRandom();

    public static void main(String[] args)
    {
        try
        {
            File file = new File("output.txt");
            File csv = new File("data.csv");
            if (file.exists())
            {
                file.delete();
                csv.delete();
            }
            file.createNewFile();
            csv.createNewFile();
            FileWriter fw = new FileWriter(file.getAbsoluteFile());
            FileWriter fwcsv = new FileWriter(csv.getAbsoluteFile());
            BufferedWriter writer = new BufferedWriter(fw);
            BufferedWriter csvWriter = new BufferedWriter(fwcsv);
            writer.write("Hash-Attack Results:\n");

            for (int i = 0; i < 22; i++)
            {
                int bitLength = BIT_LENGTH + i;
                for (int j = 0; j < 50; j++)
                {
                    Set<String> data = new HashSet<>();
                    String preImageTarget = generateHash(bitLength);
                    data.add(preImageTarget);
                    int iterations = 0;
                    int collisions = 0;
                    while (true)
                    {
                        iterations++;
                        String hash = generateHash(bitLength);
                        if (!data.add(hash) && collisions == 0)
                        {
                            collisions = iterations;
                        }
                        if (hash.equals(preImageTarget))
                        {
                            break;
                        }
                    }

                    writer.write("BIT SIZE[" + bitLength + "]                              ", 0, 15);
                    writer.write("TEST[" + j + "]:                                         ", 0, 10);
                    writer.write("Pre-Image Completed after\t" + iterations + "            ", 0, 33);
                    writer.write(" iterations and collisions completed after\t" + collisions + "                      ", 0, 50);
                    writer.write(" iterations\n", 0, 12);
                    csvWriter.write(bitLength + ", " + (j + 1) + ", " + iterations + ", " + collisions + "\r\n");

                    System.out.println("Completed bit-" + bitLength + " test: " + j);
                }
            }

            writer.close();
            csvWriter.close();
            System.out.println("DONE");
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
    }

    private static String generateHash(int bitLength)
    {
        JByte bitSet = hasher.hash(new BigInteger(130, random).toString(32), bitLength);
        return bitSet.toString();
    }
}
