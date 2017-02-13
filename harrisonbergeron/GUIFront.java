
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
	private JButton NextButton;
	private JLabel DisplayLabel;
	private JLabel BGLabel;
	private JLabel BGFridge;
	private JLabel BGRedScreenMain;
	private JLabel BGRedScreenFridge1;
	private JLabel BGRedScreenFridge2;
	
	int Iterations = 0;
	
	//sfx
	BGM bgm = new BGM();
	buzzer Buzzer = new buzzer();
	BottleBreak bottle = new BottleBreak();
	CannonSalute Cannons = new CannonSalute();
	SirenSound Siren = new SirenSound();
	DoorScreech Doors = new DoorScreech();
	CarCrash crashing = new CarCrash();
	ShotGun gunshots = new ShotGun();
	ShotGun gunshots2 = new ShotGun();
	RivetGun Rivetting = new RivetGun();
	
	public GUIFront()
	{
		super("Harrison Bergeron");
		contents = getContentPane();
		contents.setLayout(null);
		
		
		Insets insets = contents.getInsets();
		TitleLabel = new JLabel("HARRISON BERGERON");
		DisplayLabel = new JLabel("                                                     ");
		BGLabel = new JLabel(new ImageIcon("gfx/tv opening.gif"));
		BGFridge = new JLabel(new ImageIcon("gfx/fridge.jpg"));
		BGRedScreenMain = new JLabel(new ImageIcon("gfx/redscreen.jpg"));
		BGRedScreenFridge1 = new JLabel(new ImageIcon("gfx/redscreenf1.jpg"));
		BGRedScreenFridge2 = new JLabel(new ImageIcon("gfx/redscreenf2.jpg"));
		StartButton = new JButton();
		NextButton = new JButton();
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
				contents.add(NextButton);
				contents.add(DisplayLabel);
				contents.add(BGLabel);
			}
		
		});
		
		NextButton.setAction(new AbstractAction("Next")
		{
			@Override
			public void actionPerformed(ActionEvent e)
			{
				DisplayLabel.setText(LinesList(Iterations));
				Iterations++;
				
				if(Iterations == 2)
				{
					Buzzer.start();
				}
				
				if(Iterations == 3)
				{
					contents.remove(BGLabel);
					contents.revalidate();
					contents.repaint();
					contents.add(BGRedScreenMain);
					bottle.start();
				}
				if(Iterations == 4)
				{
					contents.remove(BGRedScreenMain);
					contents.revalidate();
					contents.repaint();
					contents.add(BGLabel);
				}
				if(Iterations == 13)
				{
					contents.remove(BGLabel);
					contents.revalidate();
					contents.repaint();
					contents.add(BGRedScreenMain);
					Cannons.start();
				}
				if(Iterations == 14)
				{
					contents.remove(BGRedScreenMain);
					contents.revalidate();
					contents.repaint();
					contents.add(BGLabel);
				}
				if(Iterations == 27)
				{
					contents.remove(BGLabel);
					contents.revalidate();
					contents.repaint();
					contents.add(BGRedScreenMain);	
					Siren.start();
				}
				if(Iterations == 28)
				{
					contents.remove(BGRedScreenMain);
					contents.revalidate();
					contents.repaint();
					contents.add(BGLabel);
				}
				if(Iterations == 40)
				{
					Doors.start();
				}
				
				if(Iterations == 44)
				{
					contents.remove(BGLabel);
					contents.revalidate();
					contents.repaint();
					contents.add(BGRedScreenMain);
					crashing.start();
				}
				if(Iterations == 45)
				{
					contents.remove(BGRedScreenMain);
					contents.revalidate();
					contents.repaint();
					contents.add(BGLabel);
				}
				if(Iterations == 54)
				{
					contents.remove(BGLabel);
					contents.revalidate();
					contents.repaint();
					contents.add(BGFridge);
				}
				
				if(Iterations == 55)
				{
					contents.remove(BGFridge);
					contents.revalidate();
					contents.repaint();
					contents.add(BGRedScreenFridge1);
					gunshots.start();
				}
				if(Iterations == 56)
				{
					contents.remove(BGRedScreenFridge1h);
					contents.revalidate();
					contents.repaint();
					contents.add(BGRedScreenFridge2);
					gunshots2.start();
				}
				if(Iterations == 57)
				{
					contents.remove(BGRedScreenFridge2);
					contents.revalidate();
					contents.repaint();
					contents.add(BGLabel);
				}
				if(Iterations == 63)
				{
					contents.remove(BGLabel);
					contents.revalidate();
					contents.repaint();
					contents.add(BGRedScreenMain);
					Rivetting.start();
				}
				if(Iterations == 64)
				{
					contents.remove(BGRedScreenMain);
					contents.revalidate();
					contents.repaint();
					contents.add(BGLabel);
				
				}
				
				if(Iterations == 66)
				{
				
					contents.remove(BGLabel);
					contents.revalidate();
					contents.repaint();
					contents.add(BGRedScreenMain);
					contents.remove(NextButton);
					contents.revalidate();
					contents.repaint();
				}
				
			}
		
		
		});
		
		contents.add(TitleLabel);
		contents.add(StartButton);
		
		Dimension size = TitleLabel.getPreferredSize();
		TitleLabel.setBounds(450+insets.left, 250+insets.top, size.width, size.height);
		
		size = BGLabel.getPreferredSize();
		BGLabel.setBounds(0+insets.left,0+insets.top,1000,500);
		
		size = BGFridge.getPreferredSize();
		BGFridge.setBounds(0+insets.left,0+insets.top,1000,500);
		
		size = BGRedScreenMain.getPreferredSize();
		BGRedScreenMain.setBounds(0+insets.left,0+insets.top,1000,500);
		
		size = BGRedScreenFridge1.getPreferredSize();
		BGRedScreenFridge1.setBounds(0+insets.left,0+insets.top,1000,500);
		
		size = BGRedScreenFridge2.getPreferredSize();
		BGRedScreenFridge2.setBounds(0+insets.left,0+insets.top,1000,500);
		
		size = DisplayLabel.getPreferredSize();
		DisplayLabel.setBounds(30+insets.left,150+insets.top,1000,250);
		
		size = StartButton.getPreferredSize();
		StartButton.setBounds(480+insets.left,300+insets.top,size.width,size.height);
		
		size = NextButton.getPreferredSize();
		
		size = NextButton.getPreferredSize();
		NextButton.setBounds(480+insets.left,400+insets.top,size.width,size.height);

		
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
	
	public static class buzzer extends Thread
	{
		public void run()
		{	
			try{
				SFX.buzzer();
			}catch(Exception LineUnavailableException){}
			
		}
	}
	public static class BottleBreak extends Thread
	{
		public void run()
		{
			try{
				SFX.bottle();
			}catch(Exception LineUnavailableException){}
		}		
	}
	
	public static class CannonSalute extends Thread
	{
		public void run()
		{
			try{
				SFX.cannons();
			}catch(Exception LineUnavailableException){}
		}		
	}
	
	public static class SirenSound extends Thread
	{
		public void run()
		{
			try{
				SFX.siren();
			}catch(Exception LineUnavailableException){}
		}		
	}
	
	public static class DoorScreech extends Thread
	{
		public void run()
		{
			try{
				SFX.door();
			}catch(Exception LineUnavailableException){}
		}		
	}
	
	public static class CarCrash extends Thread
	{
		public void run()
		{
			try{
				SFX.carcrash();
			}catch(Exception LineUnavailableException){}
		}		
	}
	public static class ShotGun extends Thread
	{
		public void run()
		{
			try{
				SFX.shotgun();
			}catch(Exception LineUnavailableException){}
		}		
	}
	public static class RivetGun extends Thread
	{
		public void run()
		{
			try{
				SFX.rivetgun();
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
	public String LinesList(int i)
	{
		List<String> LinesList1 = new ArrayList<String>();
		
		LinesList1.add("It was some ballerina show.");
		//Buzzer
		LinesList1.add("<html><body>\"That was a real pretty dance, that dance they just did,\" my wife, Hazel, said. My thoughts started to drift toward the<br>ballerinas -- none of them were very good. They were all burdened down with weights and faces masked. What if they weren't burd --</body></html>");
		LinesList1.add("...");
		LinesList1.add("...I tried to recover my train of thoughts, but it was too difficult. Hazel looked at me and asked me what I had heard.");
		LinesList1.add("\"Sounded like somebody hitting a bottle with a hammer,\" I said.");
		LinesList1.add("<html><body>\"It'd be interesting, I think, hearing all those sounds,\" Hazel said, looking a bit jealous. I muttered something. \"If I was the handicapper general,\" <br>she said, \"I think I'd have chimes on sunday -- just chimes. In honor of religion.\"</body></html>");
		LinesList1.add("\"I'd be able to think if it were just chimes,\" I said.");
		LinesList1.add("\"Well, I'd just make 'em real loud,\" she said. \"I think I'd make a good Handicapper General.\"");
		LinesList1.add("\"Good as anybody else.\"");
		LinesList1.add("\"Who knows better than I do what normal is?\"");
		LinesList1.add("\"Right.\"");
		LinesList1.add("I began to think of my son -- the one who they had deemed so abnormal that they decided to lock him up -- Harrison. I always wondered what he might --");
		LinesList1.add("...");
		LinesList1.add("I shut my eyes and placed my hands on my temples, it was so loud. When I opened my eyes, blurred a bit by incipient tears, I saw Hazel looking worriedly at me.");
		LinesList1.add("\"Boy! That was a doozy, wasn't it?\" she said. \"I could hear it from here.\"");
		LinesList1.add("On the TV, two of the ballerinas had collapsed, clutching their own temples.");
		LinesList1.add("\"Why don't you go rest on the sofa for a little while, honeybunch -- get that weight off your shoulders. I don't care if you're not equal with me for a little bit.\"");
		LinesList1.add("I hefted the bags a bit, weighing them.");
		LinesList1.add("\"I don't really mind it,\" I said. \"I don't even notice it, to be honest. The weight, it's become a part of me.\"");
		LinesList1.add("<html><body>\"You've been looking so tired lately,\" Hazel said, \"worn out. If only there was some way to make a hole at the bottom of the bags and just take some of the lead balls out.<br> Just a couple.\"</body></html>");
		LinesList1.add("\"Two years in prison and two-thousand dollar fine for each ball I take out,\" I reminded her, \"that ain't exactly a bargain.\"");
		LinesList1.add("\"If you could just take a few out when you come home, I mean -- you aren't competing with anybody here, you just sit around.\"");
		LinesList1.add("\"If I tried it, other people would try it. Pretty soon we'd be back in the dark ages, with everybody competing against everybody else. You wouldn't like that, would you?\"");
		LinesList1.add("\"I'd hate it,\" she said.");
		LinesList1.add("\"And there you have it. The minute people start subverting the laws, what do you think happens to society?\"");
		LinesList1.add("She opened her mouth --");
		LinesList1.add("...");
		LinesList1.add("\"...fall all apart,\" Hazel said.");
		LinesList1.add("\"What?\"");
		LinesList1.add("\"Society?\" she said. \"What we were just talking about?\"");
		LinesList1.add("\"Oh,\" I said, \"who knows?\"");
		LinesList1.add("<html><body>A news bulletin interrupted the ballerina show. For about a half a minute, his words slurred and excited, the announcer tried to talk,<br> apparently trying to say \"ladies and gentlemen\", but he eventually gave up, and handed the bulletin to a ballerina to read.</body></html>");
		LinesList1.add("\"That's all right,\" Hazel said. \"He tried. He tried the best with what God gave him. He ought to get a nice raise for trying so hard.\"");
		LinesList1.add("<html><body>\"Ladies and Gentlemen,\" the ballerina said. I imagined she had to have been beautiful, because the mask she wore was so hideous. And I <br>could tell -- she must have been the most graceful and elegant of the lot, because the weight bags she wore looked to be the same as those worn by <br>two-hundred-pound men.</body></html>");
		LinesList1.add("<html><body>And her voice -- her voice was beautiful, warm, melodious, luminous. But she stopped mid-sentence, and began again, throwing her voice as uncompetetively <br>as she could.</body></html>");
		LinesList1.add("<html><body>\"Harrison Bergeron, age fourteen,\" she said in a voice now reminiscent of a grackle's squawk, \"has just escaped from jail, where he was held on <br>suspicion of plotting to overthrow the government. He is a genius and an athlete, is under-handicapped, and should be regarded as extremely dangerous.\"</body></html>");
		LinesList1.add("<html><body>A photograph of Bergeron flashed on-screen, first in several incorrect orientations, and then finally right-side-up. He was exactly seven feet tall, and wore handicaps <br>unlike any before seen -- he wore a tremendous set of earphones, and thick, wave-lensed glasses that obscured half of his face. There was scrap metal covering <br>over most of his body. It didn't appear regulation, but instead ad hoc and hastily thrown together in place of the normal weight bags that strong people were given.</body></html>");
		LinesList1.add("To top it off, his good looks were obscured with a big red nose and random black caps on his teeth, and his brows were shaved away.");
		LinesList1.add("\"If you see this boy,\" the ballerina continued, \"do not -- I repeat, do not -- attempt to reason with him.\"");
		LinesList1.add("The bulletin was interrupted then by the sound of metal shearing -- a door being ripped from its hinges.");
		LinesList1.add("<html><body>There were screams, and the TV began to shake -- or rather, it was the camera shaking, as though in an earthquake. But it was a familiar earthquake -- one I knew, <br>because it had occupied this very house long before.</body></html>");
		LinesList1.add("It took just a moment for me to connect the dots.");
		LinesList1.add("\"By God, that's Harrison!\" I snapped.");
		LinesList1.add("...");
		LinesList1.add("<html><body>I shut my eyes, and when I opened them again, I saw Harrison -- as clownish as he looked -- occupying the center stage. The knob of the door he had torn open was still <br>in his hands, and the people in the studio cowered before him.</body></html>");
		LinesList1.add("<html><body>\"I am the Emperor!\" he roared. \"Do you hear? I am the Emperor! And all must do as I say!\" One of his feet came down, shaking the entire studio. \"Even as I stand here, <br>hobbled and handicapped, I am greater than any man who has ever lived! Now watch, watch as I become even greater!\"</body></html>");
		LinesList1.add("<html><body>The straps of his handicaps -- rated to several thousand pounds of force -- gave way instantly, like wet tissue paper, and his scrap-iron handicaps fell to the ground. He <br>shattered the lock to his head harness with his bear hands, tearing the headphones from his ears and dashing them against the wall, and following them up with the <br>glasses soon thereafter.</body></html>");
		LinesList1.add("He tossed away his clown-nose and finally revealed the full extent of his handsomeness: a chiseled jawline, strong facial features; he looked fit to be a god.");
		LinesList1.add("<html><body>\"And now I shall claim my empress! Let the first woman who dares rise take her place by my side!\" He held out a hand. Tentatively, after several seconds, one of the <br>ballerinas stood shakily. Harrison deftly removed the mask and earphones that handicapped her, revealing a stunning beauty.</body></html>");
		LinesList1.add("He removed the handicaps from the musicians who had been playing for the show.");
		LinesList1.add("\"Play your best! Show the world the meaning of 'music' and my empress and I shall dance! All who play their best will be granted honors!\"");
		LinesList1.add("<html><body>After several seconds of silence, amidst now greatly improved music, Harrison and the ballerina stood silently. They then began to dance -- gracefully, like I had <br>never seen before.</body></html>");
		LinesList1.add("The Handicapper General herself, Diana Moon Glampers, had strolled in, with confidence and haste, bearing a double barreled shotgun.");
		LinesList1.add("<html><body>I turned away, feeling suddenly nauseas, <br>and went to the fridge to get a beer.</body></html>");
		LinesList1.add("...");
		LinesList1.add("......");
		LinesList1.add("The noise suddenly stopped. When I had returned, I saw Hazel, her face tear-streaked, staring at the burnt-out TV.");
		LinesList1.add("\"You're crying,\" I pointed out.");
		LinesList1.add("\"Yeah. Something on TV was really sad. But I don't remember what,\" she said, her voice wavering a bit.");
		LinesList1.add("\"Forget sad things,\" I said.");
		LinesList1.add("\"I always do.\"");
		LinesList1.add("\"That's my girl.\"");
		LinesList1.add("...");
		LinesList1.add("\"Gee - that sounded like a doozy.\"");
		LinesList1.add("\"You can say that again.\"");
		LinesList1.add("My wife repeated herself.");
		//one last pulse
		
		return LinesList1.get(i);
	}
	
	
}