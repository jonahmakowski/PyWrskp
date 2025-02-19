package com.math;
import java.util.*;

public class math {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Enter the first number");
        String num1 = input.nextLine();

        System.out.println("Enter the oparation");
        String op = input.nextLine();

        System.out.println("Enter the other number");
        String num2 = input.nextLine();

        int num1_int = Integer.parseInt(num1);
        int num2_int = Integer.parseInt(num2);
        int aw = 0;

        if (op.equals("+")) {
            aw = num1_int + num2_int;
        }

        else if (op.equals("-")) {
            aw = num1_int - num2_int;
        }

        else if (op.equals("*")) {
            aw = num1_int * num2_int;
        }

        else if (op.equals("/")) {
            aw = num1_int * num2_int;
        }

        else {
            System.out.println("Error you incorrectly inputed the op");
            System.exit(0);
        }

        System.out.println("Here is " + num1 + ' ' + op + ' ' + num2 + ':');
        System.out.println(aw);
    }

}
