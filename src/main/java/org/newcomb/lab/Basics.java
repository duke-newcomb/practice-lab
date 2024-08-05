package org.newcomb.lab;

public class Basics {
    private String myName = "Mark";
    public void start(){
        // Data types
        int myInt = 7;
        byte myByte = 2;
        short myShort = 10;
        double myDub = 25.5;
        float myFloat = 5.5f;
        long myLong = 234_222_555l;
        boolean myBool = false;
        char myChar = 'm';
        System.out.println(myName + " is casting a double to an int: " + (int)myDub);
        char uniChar = '\u0044';
        System.out.println(uniChar);
    }
}
