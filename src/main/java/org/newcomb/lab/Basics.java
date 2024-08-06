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
        String numStr = "10";
        int myInteger = Integer.parseInt(numStr);
        System.out.println(myInteger);
    }

    public void run(){
        basics("Mark");
    }

    public void basics(String name){
        String person2;
        if((person2 = name.equals("Mark") ? "Mokie" : "Tim").equals("Mokie")){
            System.out.println("Person2 is Mokie");
        }else {
            System.out.println("Not Mokie");
        }
        int a = 7;
        int b = 4;
        if(a > 6 & b > 3){
            System.out.println("yes");
        }else{
            System.out.println("no");
        }
        if(a > 6 | b < 2){
            System.out.println("yes");
        }else{
            System.out.println("no");
        }
    }
}
