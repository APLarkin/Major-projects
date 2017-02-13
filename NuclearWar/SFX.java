

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
		Murmur();
	}
	public static void Murmur() throws LineUnavailableException, UnsupportedAudioFileException, IOException
	{
	
		Clip clip = AudioSystem.getClip();
	    AudioInputStream inputStream = AudioSystem.getAudioInputStream(new File("sounds/murmur2.wav"));
	    clip.open(inputStream);
	    clip.start(); 
	
	        // need these two lines so the program doesn't end before the sound starts
	    Scanner scanner = new Scanner(System.in);
	    scanner.next();
	
	}
	public static void nuke1() throws LineUnavailableException, UnsupportedAudioFileException, IOException
	{
	
		Clip clip = AudioSystem.getClip();
	    AudioInputStream inputStream = AudioSystem.getAudioInputStream(new File("sounds/distant_explosion.wav"));
	    clip.open(inputStream);
	    clip.start(); 
	
	        // need these two lines so the program doesn't end before the sound starts
	    Scanner scanner = new Scanner(System.in);
	    scanner.next();
	
	}
	public static void glassBreak() throws LineUnavailableException, UnsupportedAudioFileException, IOException
	{
		Clip clip = AudioSystem.getClip();
	    AudioInputStream inputStream = AudioSystem.getAudioInputStream(new File("sounds/window break.wav"));
	    clip.open(inputStream);
	    clip.start(); 
	
	        // need these two lines so the program doesn't end before the sound starts
	    Scanner scanner = new Scanner(System.in);
	    scanner.next();
	}
	public static void AAGun() throws LineUnavailableException, UnsupportedAudioFileException, IOException
	{
		Clip clip = AudioSystem.getClip();
	    AudioInputStream inputStream = AudioSystem.getAudioInputStream(new File("sounds/AA gun.wav"));
	    clip.open(inputStream);
	    clip.start(); 
	
	        // need these two lines so the program doesn't end before the sound starts
	    Scanner scanner = new Scanner(System.in);
	    scanner.next();
	}
	public static void Crash() throws LineUnavailableException, UnsupportedAudioFileException, IOException
	{
		Clip clip = AudioSystem.getClip();
	    AudioInputStream inputStream = AudioSystem.getAudioInputStream(new File("sounds/crash.wav"));
	    clip.open(inputStream);
	    clip.start(); 
	
	        // need these two lines so the program doesn't end before the sound starts
	    Scanner scanner = new Scanner(System.in);
	    scanner.next();
	}
	public static void Collapse() throws LineUnavailableException, UnsupportedAudioFileException, IOException
	{
	
		Clip clip = AudioSystem.getClip();
	    AudioInputStream inputStream = AudioSystem.getAudioInputStream(new File("sounds/02DesertWind.wav"));
	    clip.open(inputStream);
	    clip.start(); 
	
	        // need these two lines so the program doesn't end before the sound starts
	    Scanner scanner = new Scanner(System.in);
	    scanner.next();
	
	}
	public static void bgm() throws LineUnavailableException, UnsupportedAudioFileException, IOException
	{
		Clip clip = AudioSystem.getClip();
	    AudioInputStream inputStream = AudioSystem.getAudioInputStream(new File("sounds/collapse.wav"));
	    clip.open(inputStream);
	    clip.start(); 
	
	        // need these two lines so the program doesn't end before the sound starts
	    Scanner scanner = new Scanner(System.in);
	    scanner.next();
	}
	

}