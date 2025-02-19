package com.txt;
import java.io.FileNotFoundException;
import java.util.*;
import java.io.PrintWriter;

public class txt {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner input = new Scanner(System.in);
        System.out.println("Input info for the txt file");
        String info = input.nextLine();
        PrintWriter printer = new PrintWriter("info.txt");
        printer.println(info);
        printer.flush();
        printer.close();
    }
}
