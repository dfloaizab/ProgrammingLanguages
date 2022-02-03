public class GFG {
  

    static void Function1(String str, String ans)
    {
  

        if (str.length() == 0) {
            System.out.print(ans + " ");
            return;
        }
  
        for (int i = 0; i < str.length(); i++) {
  

            char ch = str.charAt(i);
  

            String ros = str.substring(0, i) + 
                         str.substring(i + 1);
  

            Function1(ros, ans + ch);
        }
    }
  

    public static void main(String[] args)
    {
        String s = "abb";
        Function1(s, "");
    }
}