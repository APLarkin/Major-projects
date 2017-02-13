
import javax.swing.JButton;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;
import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.GridBagLayout;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.image.BufferedImage;
import java.awt.Image;
import java.awt.Color;
import java.awt.Graphics;
import java.util.*;
import java.io.*;

import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.UnsupportedAudioFileException;

import javax.imageio.*;

import sun.audio.*;

import java.awt.Insets;
import java.awt.Dimension;

public class GUIFront extends JFrame
{
	private Container contents;
	private JLabel TitleLabel;
	private JButton StartButton;
	private JButton IntroNextButton;
	private JButton SchoolNextButton;
	private JButton SchoolStart;
	private JButton SubWayNextButton;
	private JButton SubWayStart;
	private JLabel DisplayLabel;
	private JLabel BGLabel;
	private JLabel BGLabel_war;
	private JLabel Flee;
	private JLabel NatGuard;
	private JLabel MetroEntry;
	private JLabel MetroStairs;
	private JLabel MetroInterior;
	
	int Iterations = 0;
	
	//sfx
	BGM bgm = new BGM();
	Nuke nuke1 = new Nuke();
	Nuke nuke2 = new Nuke();
	Nuke nuke3 = new Nuke();
	Nuke nuke4 = new Nuke();
	Nuke nuke5 = new Nuke();
	Nuke nuke6 = new Nuke();
	Nuke nuke7 = new Nuke();
	Nuke nuke8 = new Nuke();
	Nuke nuke9 = new Nuke();
	Nuke nuke10 = new Nuke();
	Nuke nuke11 = new Nuke();
	Nuke nuke12 = new Nuke();
	Nuke nuke13 = new Nuke();
	CrowdMurmur murmur = new CrowdMurmur();
	Crash crash1 = new Crash();
	GlassBreaking break1 = new GlassBreaking();
	AntiAir AAguns = new AntiAir();
	AntiAir AAguns1 = new AntiAir();
	AntiAir AAguns2 = new AntiAir();
	Collapse collapse1 = new Collapse();
	
	public GUIFront()
	{
		super("The Walls Came Crashing Down");
		contents = getContentPane();
		contents.setLayout(null);
		
		
		Insets insets = contents.getInsets();
		TitleLabel = new JLabel("<html><body>The Walls Came Crashing Down<br><center>Episode 1: Survive</center></body></html>");
		DisplayLabel = new JLabel("                                                     ");
		BGLabel = new JLabel(new ImageIcon("gfx/bg1 final.jpg"));
		BGLabel_war = new JLabel(new ImageIcon("gfx/bg war.jpg"));
		Flee = new JLabel(new ImageIcon("gfx/flee.jpg"));
		NatGuard = new JLabel(new ImageIcon("gfx/NatGuard.jpg"));
		MetroEntry = new JLabel(new ImageIcon("gfx/metro.jpg"));
		MetroStairs = new JLabel(new ImageIcon("gfx/escalator.jpg"));
		/*
		MetroInterior = new JLabel(new ImageIcon("gfx/interior.jpg"));
		*/
		
		StartButton = new JButton();
		IntroNextButton = new JButton();
		SubWayNextButton = new JButton();
		SubWayStart = new JButton();
		SchoolNextButton = new JButton();
		SchoolStart = new JButton();
		DisplayLabel.setForeground(Color.WHITE);
		
		StartButton.setAction(new AbstractAction("Begin")
		{
			@Override
			public void actionPerformed(ActionEvent e)
			{
				//music();
				bgm.start();
				contents.remove(StartButton);
				contents.revalidate();
				contents.repaint();
				contents.remove(TitleLabel);
				contents.add(IntroNextButton);
				contents.add(DisplayLabel);
				contents.add(BGLabel);
				nuke1.start();
				murmur.start();
			}
		
		});
		
		IntroNextButton.setAction(new AbstractAction("Next")
		{
			@Override
			public void actionPerformed(ActionEvent e)
			{
				DisplayLabel.setText(IntroList(Iterations));
				Iterations++;
				
				if(Iterations == 6)
				{
					nuke2.start();
					
				}
				if(Iterations == 7)
				{
					contents.remove(BGLabel);
					contents.revalidate();
					contents.repaint();
					contents.add(BGLabel_war);
				}
				if(Iterations == 10)
				{
					contents.remove(BGLabel_war);
					contents.revalidate();
					contents.repaint();
					contents.add(BGLabel);
				}
				if(Iterations == 19)
				{
					contents.remove(IntroNextButton);
					contents.remove(BGLabel);
					contents.revalidate();
					contents.repaint();
					contents.add(SubWayStart);
					contents.add(SchoolStart);
					contents.add(BGLabel);
				}
			}
			
				
		
		
		});
		
		SubWayNextButton.setAction(new AbstractAction("Next")
		{
			@Override
			public void actionPerformed(ActionEvent e)
			{
				DisplayLabel.setText(SubWayPartOne(Iterations));
				Iterations++;
				if(Iterations == 0)
				{
					AAguns1.start();
				}
				if(Iterations == 2)
				{
					//glass break
					break1.start();
				}
				if(Iterations == 3)
				{
					contents.remove(BGLabel);
					contents.revalidate();
					contents.repaint();
					contents.add(Flee);
				}
				if(Iterations == 4)
				{
					//next scene
					contents.remove(Flee);
					contents.revalidate();
					contents.repaint();
					contents.add(NatGuard);
					//AA gun
					AAguns2.start();
				}
				if(Iterations == 6)
				{
					//Crash sound
					crash1.start();
					//explosion
					nuke3.start();
				}
				if(Iterations == 8)
				{
					//Exterior of emtro
					contents.remove(NatGuard);
					contents.revalidate();
					contents.repaint();
					contents.add(MetroEntry);
				}
				if(Iterations == 9)
				{
					//stairs of metro
					contents.remove(MetroEntry);
					contents.revalidate();
					contents.repaint();
					contents.add(MetroStairs);
					//explosion
					nuke4.start();
				}
				if(Iterations == 10)
				{
					//Interior of metro
					/*
					contents.remove(MetroStairs);
					contents.revalidate();
					contents.repaint();
					contents.add(MetroInterior);
					*/
					//AA gun
					AAguns.start();
				}
				if(Iterations == 11)
				{
				
					//explosion
					nuke5.start();
				}
				if(Iterations == 12)
				{
					//explosion
					nuke6.start();
				}
				if(Iterations == 13)
				{
					//explosion
					nuke7.start();
				}
				if(Iterations == 14)
				{
					//explosion
					nuke8.start();
					//collapse sound
					collapse1.start();
				}
				if(Iterations == 18)
				{
					//explosion
					nuke9.start();
				}
				if(Iterations == 20)
				{
					//explosion
					nuke10.start();
				}
				if(Iterations == 21)
				{
					//explosion
					nuke11.start();
				}
				if(Iterations == 24)
				{
					//explosion
					nuke12.start();
				}
				if(Iterations == 26)
				{
					//explosion
					nuke13.start();
				}
				if(Iterations == 27)
				{
					System.exit(0);
				}
			}
			
		});
		SubWayStart.setAction(new AbstractAction("Run to the subway")
		{
			@Override
			public void actionPerformed(ActionEvent e)
			{
				Iterations++;
				if(Iterations == 20)
				{
					contents.remove(BGLabel);
					contents.remove(SchoolStart);
					contents.remove(SubWayStart);
					contents.revalidate();
					contents.repaint();
					contents.add(SubWayNextButton);
					contents.add(BGLabel);
					Iterations = 0;
				}
			}
			
		});
		
		SchoolNextButton.setAction(new AbstractAction("Next")
		{
			@Override
			public void actionPerformed(ActionEvent e)
			{
				DisplayLabel.setText(SchoolList(Iterations));
				Iterations++;
				if(Iterations == 0)
				{
					nuke4.start();
				}
				if(Iterations == 3)
				{
					nuke5.start();
				}
				if(Iterations == 6)
				{
					nuke6.start();
				}
				if(Iterations == 1)
				{
					contents.remove(BGLabel);
					contents.revalidate();
					contents.repaint();
					contents.add(Flee);
				}
				if(Iterations == 8)
				{
					System.exit(0);
				}
				
			}
			
		});
		
		
		SchoolStart.setAction(new AbstractAction("Run to the school")
		{
			@Override
			public void actionPerformed(ActionEvent e)
			{
				Iterations++;
				if(Iterations == 20)
				{
					contents.remove(BGLabel);
					contents.remove(SchoolStart);
					contents.remove(SubWayStart);
					contents.revalidate();
					contents.repaint();
					contents.add(SchoolNextButton);
					contents.add(BGLabel);
					Iterations = 0;
				}
			}
			
		});
		
		contents.add(TitleLabel);
		contents.add(StartButton);
		
		Dimension size = TitleLabel.getPreferredSize();
		TitleLabel.setBounds(400+insets.left, 200+insets.top, size.width, size.height);
		
		size = BGLabel.getPreferredSize();
		BGLabel.setBounds(0+insets.left,0+insets.top,1000,500);

		size = BGLabel_war.getPreferredSize();
		BGLabel_war.setBounds(0+insets.left,0+insets.top,1000,500);
		
		size = Flee.getPreferredSize();
		Flee.setBounds(0+insets.left,0+insets.top,1000,500);
		
		size = NatGuard.getPreferredSize();
		NatGuard.setBounds(0+insets.left,0+insets.top,1000,500);
		
		size = MetroEntry.getPreferredSize();
		MetroEntry.setBounds(0+insets.left,0+insets.top,1000,500);
		
		size = MetroStairs.getPreferredSize();
		MetroStairs.setBounds(0+insets.left,0+insets.top,1000,500);
		
		/*
		size = MetroInterior.getPreferredSize();
		MetroInterior.setBounds(0+insets.left,0+insets.top,1000,500);
		*/
		
		size = DisplayLabel.getPreferredSize();
		DisplayLabel.setBounds(30+insets.left,150+insets.top,1000,250);
		
		size = StartButton.getPreferredSize();
		StartButton.setBounds(480+insets.left,300+insets.top,size.width,size.height);

		size = IntroNextButton.getPreferredSize();
		IntroNextButton.setBounds(480+insets.left,400+insets.top,size.width,size.height);
		
		size = SubWayNextButton.getPreferredSize();
		SubWayNextButton.setBounds(480+insets.left,400+insets.top,size.width,size.height);
		
		size = SchoolNextButton.getPreferredSize();
		SchoolNextButton.setBounds(480+insets.left,400+insets.top,size.width,size.height);
		
		size = SubWayStart.getPreferredSize();
		SubWayStart.setBounds(280+insets.left,400+insets.top,size.width,size.height);
		
		size = SchoolStart.getPreferredSize();
		SchoolStart.setBounds(680+insets.left,400+insets.top,size.width,size.height);
		
		setSize(1000,500);
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
	}
	
	public static class BGM extends Thread
	{
		public void run()
		{	
			try{
				SFX.bgm();
			}catch(Exception LineUnavailableException){}	
		}
	}
	public static class CrowdMurmur extends Thread
	{
		public void run()
		{	
			try{
				SFX.Murmur();
			}catch(Exception LineUnavailableException){}	
		}
	}
	public static class Nuke extends Thread
	{
		public void run()
		{	
			try{
				SFX.nuke1();
			}catch(Exception LineUnavailableException){}	
		}
	}
	public static class GlassBreaking extends Thread
	{
		public void run()
		{	
			try{
				SFX.glassBreak();
			}catch(Exception LineUnavailableException){}	
		}
	}
	public static class AntiAir extends Thread
	{
		public void run()
		{	
			try{
				SFX.AAGun();
			}catch(Exception LineUnavailableException){}	
		}
	}
	public static class Crash extends Thread
	{
		public void run()
		{	
			try{
				SFX.Crash();
			}catch(Exception LineUnavailableException){}	
		}
	}
	public static class Collapse extends Thread
	{
		public void run()
		{	
			try{
				SFX.Collapse();
			}catch(Exception LineUnavailableException){}	
		}
	}

	public static void main(String[] args)
	{
		new GUIFront();
		
	}
	
	/*
	public static void music()
	{
		AudioPlayer MGP = AudioPlayer.player;
		AudioStream BGM;
		AudioData MD;
		
		ContinuousAudioDataStream loop = null;
		
		try{
			BGM = new AudioStream(new FileInputStream("sounds/02DesertWind.wav"));
			MD = BGM.getData();
			loop = new ContinuousAudioDataStream(MD);
		}catch(IOException error){}
		
		MGP.start(loop);
	}
	*/
	public String IntroList(int i)
	{
		List<String> LinesList1 = new ArrayList<String>();
		
		//distant explosion
		//murmuring
		LinesList1.add("\"Did you hear something?\" my best friend asked. We were taking a break from work, hanging out in the company lounge while we ate our lunches.");
		LinesList1.add("\"No,\" I say. He pensively gazed from the window as he ate, watching the passers-by.");
		LinesList1.add("We were high-ranking employees of one of America's largest contractors. For fallout shelters -- I oversaw the North East, and my buddy Kevin oversaw the Midatlantic.");
		LinesList1.add("It was a well-paying job.");
		LinesList1.add("The company was called UniTech, short for Unified Systems Technologies.");
		//pic of combat
		//another distant explosion
		LinesList1.add("Business had been booming for us recently -- the war with China fueled fears of nuclear holocaust, and people contracted us to build shelters for them.");
		LinesList1.add("State agencies also approached us with contracts.");
		LinesList1.add("Of course, some call this profiteering.");
		LinesList1.add("The higher-ups insisted it was for the betterment of the country. The civilians, they thought it was making money off the bodies of the dead soldiers in China.");
		//Return to original scene
		LinesList1.add("\"There it is again,\" Kevin said, butting into my train of thought. I glanced around and noticed that some of the others had perked their heads up as well.");
		LinesList1.add("<html><body>\"I think you're hearing things,\" I said. He grimaced and looked around.<br>\"Am I the only one hearing that thumping noise?\" he shouted into the murmuring crowd. Some of them nodded their head, and he looked at me, opening his mouth to say something.");
		//one more explosion
		//Jets scream overhead
		//Distant air raid siren
		LinesList1.add("All of a sudden, the cafeteria exploded into chaos.");
		//Screaming begins
		LinesList1.add("People were rushing out the door as the explosions got louder and louder, and more frequent, and jets soared by low overhead.");
		LinesList1.add("My heart suddenly leapt up into my throat.");
		LinesList1.add("\"What do we do?\" Kevin screamed. I realized time was about to run out for us.");
		LinesList1.add("We were going to die. In a nuclear war we never thought would come.");
		LinesList1.add("How had their bombers even made it to DC?");
		LinesList1.add("\"Hey!\" Kevin shouted again. I looked up. \"What the hell do we do?\" he asked again.");
		LinesList1.add("We could hightail it. Down to the school a ways away, a certified fallout shelter. Or there was a subway station nearby we could run to.");
		LinesList1.add("");
		//one last pulse
		
		return LinesList1.get(i);
	}
	public String SubWayPartOne(int i)
	{
		List<String> LinesList1 = new ArrayList<String>();
		
		//conelrad
		LinesList1.add("\"Follow me!\" I said.");
		LinesList1.add("The doors were clogged with people. Kevin and I picked up some chairs nearby and -- ");
		//Glass shattering'
		LinesList1.add("It was lucky we were on the ground floor. If we had stayed in our office thirty stories up -- there likely wouldn't have been anything we could do.");
		LinesList1.add("The streets were in chaos. The National Guard or Army had been called out to keep order during the Food Riots a week beforehand, but they couldn't keep order in this kind of chaos, with people clambering over the barricades.");
		//street view
		//look toward the exploding horizon
		//look toward the subway station
		LinesList1.add("We joined the rush, sticking close to the walls as we moved. I was leading, Kevin kept close behind me.");
		//Crash
		LinesList1.add("A plane, a Chinese plane, had slammed into a building nearby. Debris went flying, and the street was engulfed in dust.");
		LinesList1.add("Finally, down the street in the same direction the crowd was headed, we could see it.");
		//Show outside of the subway
		LinesList1.add("");
		//Show stairs of subway
		LinesList1.add("");
		//Show subway interior.
		LinesList1.add("And not a moment too soon.");
		//Massive explosion.
		LinesList1.add("The subway shook with each successive hit.");
		//Another one
		LinesList1.add("It seemed never-ending.");
		//Another hit.
		LinesList1.add("We all moved away from the entry stairwell and toward the tracks, where it was presumably safer. There were hundreds of us -- perhaps in excess of a thousand, and there was a low, worried murmur throughout the building.");
		//Another hit
		//Collapse sound.
		LinesList1.add("Dust suddenly exploded from the way Kevin and I had run down.");
		LinesList1.add("\"Everybody listen up!\" somebody shouted, trying to speak over the crowd. \"This is a worst-case scenario,\" he said. I looked up and saw some young man in combat armor standing up on top of a train car.");
		//hit
		LinesList1.add("\"I know it's scary,\" he said, \"but if we remain calm and follow the practices we all had drilled into us in our lifetime, we will make it out of this alive.\"");
		//hit
		LinesList1.add("\"My family's out there!\" somebody shouted at him. Hushed agreement from the rest of the crowd followed. \"We can't just stay here -- we have to go look for them!\"");
		LinesList1.add("\"Hey, I get it!\" the soldier shouted back. \"If you want to leave, you can find a way out -- one of the entrances down the line is probably intact.\"");
		//hit
		LinesList1.add("\"But chances are,\" he went on, \"it's going to be highly irradiated out there. You hear that?\"");
		//hit
		LinesList1.add("\"Those are nuclear bombs. This isn't some random bombing run, this is... an end of the world scenario.\" He paused for effect. \"It's very likely that if you had family in DC, they're all dead. If you had family anywhere within a twenty miles, they're probably dead if they weren't able to get to a shelter in time.\"");
		LinesList1.add("Kevin had gone to sit down while the guy was talking.");
		LinesList1.add("\"And if you go out there right now, with the radiation still in the air and bombs still falling, you'll probably die as well. But it's your choice. We can't keep you here.\"");
		//hit
		LinesList1.add("\"I doubt we're going to be going anywhere any time soon,\" Kevin said. I took a seat on the edge of the platform next to him. \"I think the life we once knew is dead now.\"");
		LinesList1.add("\"I know,\" I said. I shook my head. I was lucky -- I didn't really have a next-of-kin, no family and only a few friends to worry about.");
		//hit
		LinesList1.add("We didn't have blankets or anything, but I sure as hell wasn't about to walk into the firestorm above.");
		LinesList1.add("I took off my blazer and laid it out behind me before laying on top of it and using the crux of my arm as a makeshift pillow. Sure, it wasn't comfortable.");
		LinesList1.add("But I don't think a nuclear war was ever supposed to be.");
		//hit
		LinesList1.add("");
		//one last pulse
		
		return LinesList1.get(i);
	}
	public String SchoolList(int i)
	{
		List<String> LinesList1 = new ArrayList<String>();
		
		//hit
		LinesList1.add("\"Follow me!\" I shouted.");
		LinesList1.add("The school was some ways away, in the opposite direction that everyone was running. Kevin tried to keep up with me but ultimately we were separated in the rush.");
		//hit
		LinesList1.add("I don't know what happened to him.");
		LinesList1.add("I must have spent twenty minutes looking around, shouting for him, but Kevin was gone.");
		LinesList1.add("I had wasted too much time looking for him.");
		//hit
		LinesList1.add("It was too late. The droning of the bombers grew ever nearer.");
		LinesList1.add("I could barely even blink when the shape falling out of the sky became recognizable.");
		LinesList1.add("");
		//Massive explosion
		LinesList1.add("");
		//one last pulse
		
		return LinesList1.get(i);
	}
	
	
}