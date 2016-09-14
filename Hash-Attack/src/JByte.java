import java.util.BitSet;

public class JByte extends BitSet
{
    private int bitLength;

    public JByte(int bitLength)
    {
        super(bitLength);
        this.bitLength = bitLength;
    }

    @Override
    public String toString()
    {
        String bitString = "";
        for (int i = 0; i < this.bitLength; i++)
        {
            if (this.get(i))
            {
                bitString += "1";
            }
            else
            {
                bitString += "0";
            }
        }
        return bitString;
    }
}
