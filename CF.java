import java.io.*;
import java.util.*;
import java.util.regex.*;

public class CF {
    public static void main(String[] args) {
        try {
            FileReader reader = new FileReader("lvl3-1.inp");
            int character;
 
            while ((character = reader.read()) != -1) {
                System.out.print((char) character);
            }
            reader.close();
 
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}