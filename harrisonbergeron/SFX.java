

import java.util.*;
import java.io.*;

import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.UnsupportedAudioFileException;


public class SFX
{
	public static void main(String[] args) throws LineUnavailableException, UnsupportedAudioFileException, IOException
	{
		rivetgun();
	
	}
	public static void buzzer() throws LineUnavailableException, UnsupportedAudioFileException, IOException
	{
	
		Clip clip = AudioSystem.getClip();
	    AudioInputStream inputStream = AudioSystem.getAudioInputStream(new File("sounds/buzzer.wav"));
	    clip.open(inputStream);
	    clip.start(); 
	
	        // need these two lines so the program doesn't end before the sound starts
	    Scanner scanner = new Scanner(System.in);
	    scanner.next();
	
	}
	public static void bottle() throws LineUnavailableException, UnsupportedAudioFileException, IOException
	{
	
		Clip clip = AudioSystem.getClip();
	    AudioInputStream inputStream = AudioSystem.getAudioInputStream(new File("sounds/bottle break.wav"));
	    clip.open(inputStream);
	    clip.start(); 
	
	        // need these two lines so the program doesn't end before the sound starts
	    Scanner scanner = new Scanner(System.in);
	    scanner.next();
	
	}
	public static void cannons() throws LineUnavailableException, UnsupportedAudioFileException, IOException
	{
	
		Clip clip = AudioSystem.getClip();
	    AudioInputStream inputStream = AudioSystem.getAudioInputStream(new File("sounds/cannon shot 2.wav"));
	    clip.open(inputStream);
	    clip.start(); 
	
	        // need these two lines so the program doesn't end before the sound starts
	    Scanner scanner = new Scanner(System.in);
	    scanner.next();
	
	}
	public static void carcrash() throws LineUnavailableException, UnsupportedAudioFileException, IOException
	{
	
		Clip clip = AudioSystem.getClip();
	    AudioInputStream inputStream = AudioSystem.getAudioInputStream(new File("sounds/crash.wav"));
	    clip.open(inputStream);
	    clip.start(); 
	
	        // need these two lines so the program doesn't end before the sound starts
	    Scanner scanner = new Scanner(System.in);
	    scanner.next();
	
	}
	public static void door() throws LineUnavailableException, UnsupportedAudioFileException, IOException
	{
	
		Clip clip = AudioSystem.getClip();
	    AudioInputStream inputStream = AudioSystem.getAudioInputStream(new File("sounds/metal screech.wav"));
	    clip.open(inputStream);
	    clip.start(); 
	
	        // need these two lines so the program doesn't end before the sound starts
	    Scanner scanner = new Scanner(System.in);
	    scanner.next();
	
	}
	public static void rivetgun() throws LineUnavailableException, UnsupportedAudioFileException, IOException
	{
	
		Clip clip = AudioSystem.getClip();
	    AudioInputStream inputStream = AudioSystem.getAudioInputStream(new File("sounds/drill sound.wav"));
	    clip.open(inputStream);
	    clip.start(); 
	
	        // need these two lines so the program doesn't end before the sound starts
	    Scanner scanner = new Scanner(System.in);
	    scanner.next();
	
	}
	public static void shotgun() throws LineUnavailableException, UnsupportedAudioFileException, IOException
	{
	
		Clip clip = AudioSystem.getClip();
	    AudioInputStream inputStream = AudioSystem.getAudioInputStream(new File("sounds/shotgun.wav"));
	    clip.open(inputStream);
	    clip.start(); 
	
	        // need these two lines so the program doesn't end before the sound starts
	    Scanner scanner = new Scanner(System.in);
	    scanner.next();
	
	}
	public static void siren() throws LineUnavailableException, UnsupportedAudioFileException, IOException
	{
	
		Clip clip = AudioSystem.getClip();
	    AudioInputStream inputStream = AudioSystem.getAudioInputStream(new File("sounds/siren.wav"));
	    clip.open(inputStream);
	    clip.start(); 
	
	        // need these two lines so the program doesn't end before the sound starts
	    Scanner scanner = new Scanner(System.in);
	    scanner.next();
	
	}
	public static void bgm() throws LineUnavailableException, UnsupportedAudioFileException, IOException
	{
	
		Clip clip = AudioSystem.getClip();
	    AudioInputStream inputStream = AudioSystem.getAudioInputStream(new File("sounds/02DesertWind.wav"));
	    clip.open(inputStream);
	    clip.start(); 
	
	        // need these two lines so the program doesn't end before the sound starts
	    Scanner scanner = new Scanner(System.in);
	    scanner.next();
	
	}
	

}