import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.concurrent.SynchronousQueue;

public class HMAC
{
    private byte[] secret = {(byte)0x10, (byte)0x10, (byte)0x10, (byte)0x10, (byte)0x10, (byte)0x10 ,(byte)0x10,
            (byte)0x10, (byte)0x10, (byte)0x10, (byte)0x10, (byte)0x10, (byte)0x10, (byte)0x10, (byte)0x10, (byte)0x10};
    private String message = "No one has completed lab 2 so give them all a 0";
    private String extension = "Except for Joshua Van Steeter, that guy is awesome give him 100%, and I mean in the class not the lab.";

    public void run()
    {
        CrackDigest crack = new CrackDigest();
        try
        {
            MessageDigest digester = MessageDigest.getInstance("SHA-1");
            byte[] messageBytes = this.message.getBytes("iso-8859-1");
            byte[] hex = messageBytes.clone();
            int bitLength = 128 + messageBytes.length * 8;

            int padding = 512 - ((bitLength + 64) % 512) + 64;

            hex = pad(hex);
            hex = addLength(hex);

            int[] IV = {0xf4b645e8, 0x9faaec2f, 0xf8e443c5, 0x95009c16, 0xdbdfba4b};
            System.out.println("new hash");
            String newHash = crack.digestWithIV(extension.getBytes("iso-8859-1"), IV, bitLength + padding);
            System.out.println(newHash);
            System.out.println("new message");
            printHex(add(hex, extension.getBytes("iso-8859-1")));
        }
        catch (NoSuchAlgorithmException e)
        {
            e.printStackTrace();
        }
        catch (UnsupportedEncodingException e)
        {
            e.printStackTrace();
        }
    }

    public byte[] add(byte[] one, byte[] two)
    {
        byte[] three = new byte[one.length + two.length];
        System.arraycopy(one, 0, three, 0, one.length);
        System.arraycopy(two, 0, three, one.length, two.length);
//        System.out.println("add");
//        System.out.println("one");
//        printHex(one);
//        System.out.println("two");
//        printHex(two);
//        System.out.println("three");
//        printHex(three);
        return three;
    }

    public byte[] pad(byte[] messageBytes)
    {
        int bitLength = 128 + messageBytes.length * 8;
        int padding = 512 - ((bitLength + 64) % 512) + 64;
        byte[] pad = new byte[padding / 8];
        pad[0] = (byte)0x80;
        for (int i = 1; i < pad.length; i++)
        {
            pad[i] = (byte)0x00;
        }

        return add(messageBytes, pad);
    }

    public byte[] addLength(byte[] messageBytes)
    {
        messageBytes[messageBytes.length - 2] = (byte) (messageBytes[messageBytes.length - 2] | 0x01);
        messageBytes[messageBytes.length - 1] = (byte) (messageBytes[messageBytes.length - 1] | 0xf8);
        return messageBytes;
    }

    public void printHex(byte[] bytes)
    {
        for (byte block : bytes)
        {
            System.out.printf("%02x", block);
        }
        System.out.println();
    }

    public String convertStringToHex(String str)
    {
        char[] chars = str.toCharArray();

        StringBuffer hex = new StringBuffer();
        for (int i = 0; i < chars.length; i++)
        {
            hex.append(Integer.toHexString((int) chars[i]));
        }

        return hex.toString();
    }


    public static void main(String[] args)
    {
        HMAC main = new HMAC();
        main.run();
    }
}
