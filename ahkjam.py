import ahk
import random
import time

bpm = 60				# change this to whatever bpm you like
events = 300				# playback will consist of this many sound 'events' 
stay_back_forward = [0.4, 0.6, 1.0]    	# cumulative for the probabilities [0.4, 0.2, 0.4]
same_or_reroll_position = [0.6, 1.0]	# cumulative for the probabilities [0.6, 0.4]
same_or_reroll_duration = [0.5, 1.0]	# cumulative for the probabilities [0.5, 0.5]


qnote = 60.0/bpm
durations = [qnote * 2, qnote, qnote / 2, qnote / 4, qnote * 2 / 3, qnote * 2 / 5, qnote *2 / 7, qnote * 4 / 9]
interval = durations[random.randint(0,7)]
position = random.randint(18, 251)     # where 18 is the leftmost end of the transport bar, and 251 the rightmost
keystroke = 'x'

ahk.start()				
ahk.ready() 				
ahk.execute('Esc::\nSend v\nExitApp')  		# 'safe word' / key is Esc
ahk.execute('SetMouseDelay, 0')
ahk.execute('SetKeyDelay, 0')
ahk.execute('WinActivate, ahk_class Winamp v1.x')
ahk.execute('Click 108,62')  		# clicks volume to 0%
ahk.execute('Send ' + keystroke)

for x in range(0, events):
	if random.random() > same_or_reroll_position[0]:
		position = random.randint(18, 251)
	if random.random() > same_or_reroll_duration[0]:
		interval = durations[random.randint(0,7)]
	p = random.random()
	if p < stay_back_forward[0]:
		keystroke = 'x'				# where 'x' is the keyboard shortcut for 'play' (on Winamp it restarts playing track)
	elif p < stay_back_forward[1]:
		keystroke = 'z'				# where 'z' is the shortcut for 'previous track' (on Winamp, if it is already on very first track, no harm done)
	else:
		keystroke = 'b'				# where 'b' is the shortcut for 'previous track' (on Winamp, if it is already on very last track, no harm done)
	ahk.execute('Click 108,62')  	# volume 0%
	ahk.execute('Send ' + keystroke)
	ahk.execute('Click ' + str(position) + ',75')
	ahk.execute('Click 170,62')  	# volume 100%    
	time.sleep(interval)
	
ahk.execute('Send v')			# stop
ahk.execute('ExitApp')
