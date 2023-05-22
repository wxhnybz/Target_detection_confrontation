package com.wzy;
import com.wzy.utils.Point;
import com.wzy.utils.ColorPoint;
import sun.nio.ch.sctp.SctpNet;

import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Scanner;
interface Role{
    public void greet();
    public void move();
    public int getSpeed();
}

interface Hero extends Role{
    public void attack();
}

class Zeus implements Hero{
    private  final  String name = "Zeus";
    public void greet(){
        System.out.println(name+": Hi");
    }
    public void move() {
        System.out.println(name+": Move!");
    }

    public int getSpeed() {
        return 10;
    }
    public void attack(){
        System.out.println(name+": I attack");
    }
}

class Athena implements Hero{
    private  final  String name = "Athena";
    public void greet(){
        System.out.println(name+": Hi");
    }
    public void move() {
        System.out.println(name+": Move!");
    }

    public int getSpeed() {
        return 10;
    }
    public void attack(){
        System.out.println(name+": I attack");
    }
}
//接口也算一个基类
public class Main {
    public static void  main(String[] args){
    Scanner sc = new Scanner(System.in);
        System.out.println("请选择你的英雄");
        String name = sc.next();
        Hero hero = new Zeus();
     if(name.equals("Zeus"))hero = new Zeus();
    else if(name.equals("Athena"))hero = new Athena();
    else hero = new Zeus();
        hero.greet();


    }

}