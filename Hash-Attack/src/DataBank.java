import java.util.HashSet;
import java.util.Set;

public class DataBank
{
    private Set<String> data;

    public DataBank()
    {
        data = new HashSet();
    }

    public void add(String value)
    {
        data.add(value);
    }
}
