#import java.util.*;

#public class Candyshop{
#  public static void main(String... args){
#    ArrayList<Object> arrayList = new ArrayList<Object>();
#    arrayList.add("Cupcake");
#    arrayList.add(2);
#    arrayList.add("Brownie");
#    arrayList.add(false);

#    // Accidentally we added "2" and "false" to the list.
#    // Your task is to change from "2" to "Croissant" and change from "false" to "Ice cream"
#    // No, don't just remove the lines

#    System.out.println(arrayList);
# }
#}

list = ["Cupcake", 2, "Brownie", "false"]
list[1] = "Croissant"
list[3] = "Ice cream"

print(list)
