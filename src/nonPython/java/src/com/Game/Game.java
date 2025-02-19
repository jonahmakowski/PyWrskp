package com.Game;
import java.util.*;

public class Game {
    public static void main(String[] args) {
        //player info

        Scanner input = new Scanner(System.in);
        System.out.println("What is your name?");
        String name= input.nextLine();
        int health = 100;
        if (name.equals("Jonah")) {
            health = health * 2;
        }
        System.out.println("You have " + health + " hp.");
        System.out.println("The attacks are:");
        System.out.println("super - with 10 damage");

        // monster info

        int monster_health = 100;
        System.out.println("The monster has " + monster_health + " hp.");

        String attack;

        while (monster_health > 0 && health > 0) {
            System.out.println("What attack do you want to use?");
            attack = input.nextLine();
            if (attack.equals("super")) {
                monster_health = monster_health - 10;
                System.out.println("You did 10 damage the monster now has " + monster_health + " hp");
            }
            health = health - 10;
            System.out.println("The monster did 10 damage");
            System.out.println("You now have " + health);
        }
    }
}
