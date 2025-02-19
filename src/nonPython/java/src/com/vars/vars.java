package com.vars;
import java.util.Scanner;

public class vars {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("What would you like to print?");

        String print = input.nextLine();
        System.out.println("You wanted to print: " + print);

        var num = 5;
        String str = "Hello!";
        var dec = 5.5;

        System.out.println(num);
        System.out.println(str);
        System.out.println(dec);

    }
}
