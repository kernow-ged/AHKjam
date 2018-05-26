# AHKjam

A musical score in Python, for Winamp & Autohotkey.   

In the event that anyone wants to replicate this very peculiar & particular setup, I'll leave this up here.   

I still use **[Winamp v. 5.666](http://forums.winamp.com/showthread.php?t=373755)** as my music player, although it is not maintained any more. So this is a script to abuse Winamp into making a sound collage out of whatever audio files you supply it, inspired by the work of many 20th/21st century electronic and sampling artists; check out Jon Leidecker's Variations series of podcasts (https://rwm.macba.cat/en/variations_tag/) for an idea of where this project is coming from.   

It uses **Autohotkey**, in the form of **Pyahk**, a Python library wrapping the Autohotkey DLL (https://pyahk.readthedocs.io), to spam Winamp with hyperspeed mouse clicks and key presses in order to play back random fragments of sound. You can find the DLL at https://hotkeyit.github.io/v2/ rather than the links suggested on the Pyahk page. It is the DLL in the Win32a folder that you want to be using.   

The instance of Winamp needs to be running (but not necessarily playing) before you run the script. Load up a whole bunch of soundfiles in there and then hit Ctrl-Shift-R to randomise your list.  

Before you start the script, remember that you can hit Esc at any time to cancel it if you need your mouse and keyboard back. What will happen is that your mouse will go like the clappers, clicking away on its own to seek out random bits of the playlist. The key presses 'z', 'x' and 'b' for previous track, play and next track are also being fired off at a rate no human operator could match. The net effect is that the script jumps around wildly between and within tracks, with elements of twiddling a dial in between stations crossed with an element of phrase sampling. It's also fun to watch the sliders jumping wildly around, giving an element of 'virtual physicality' to the proceedings.  

The Python script is short, simple and speaks for itself. The method for deciding what action to take next is pretty basic, sometimes it repeats a bit and sometimes it doesn't! You could easily adapt the script for another music player by inspecting where the pixel locations for the endpoints of the volume and transport bars for the player are, using e.g. **AutoIt Window Spy**, and also changing the keyboard shortcuts in the code.  

The example.mp3 is a result of loading up Winamp with a miscellaneous load of samples (home-recorded bits & bobs, selections from old sample packs and the like) and just letting the script run for a bit. For recording the output I use [Audacity's WASAPI loopback feature](https://manual.audacityteam.org/man/tutorial_recording_computer_playback_on_windows.html#wasapi) - just press record before running the Python script and the actual recording will start when it first receives some digital audio from the loopback interface.  
