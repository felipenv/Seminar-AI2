# Team2: Yuu Sakaguchi, Felipe Vianna, Chembrolu Surya
import numpy as np
import pandas as pd

#  Given a sequence of a path, generates into Ozocode in XML.

# example
#path = [1,2,7,12,12,12,12,12,12,12,12,12,12,13,14,19,19,19,19,19,14,9,4]
#path = [2,3,4,9,14,19,19,19,19,19,24,23,22,17,12,12,12,12,12,12,12,12,12,12,7,2,3,4,5]
#path = [1,2,7,12,12,12,12,12,12,12,12,12,12,13,14,19,19,19,19,19,14,9,4]
path = [2,3,4,9,14,19,19,19,19,19,14,9,8,7,12,12,12,12,12,12,12,12,12,12,7,2,3,4,5]

print("PATH: ", path)

# Generate XML
f = open('ozocode.txt', "w", encoding='UTF-8')
f.write('<xml xmlns="http://www.w3.org/1999/xhtml">')

block = []
direction = "S"
curr = path[0]
# say numbers 3, 2, 1
f.write('<block type="ozobot_evo_say_number" id="lu@~[I_4[uZ^6%d)neFh" x="49" y="55"><value name="VALUE">' +
		'<block type="math_number" id="4g;K93M!#E]LtL,;?pjU"><field name="NUM">3</field></block></value>' +
		'<next><block type="ozobot_evo_say_number" id="/P5cy0ZUb`/W!X|*5W[-"><value name="VALUE">' +
		'<block type="math_number" id="~.IVmuWz3hIbm?$ho$SC"><field name="NUM">2</field></block></value>' +
		'<next><block type="ozobot_evo_say_number" id="v7|Irx`qQ88z#/RU~S$w"><value name="VALUE">' +
		'<block type="math_number" id="6U{JQ0iNCRzi]OpR_Ub8"><field name="NUM">1</field></block></value><next>')
f.write('<block type="ozobot_go_to_next_intersection" id="1"><next>')

for node in range(1,len(path)):
	#print(path[node])

	if path[node]-curr == 1:
		if direction=="S":
			f.write('<block type="ozobot_choose_way_at_intersection" id="2"><field name="DIRECTION">DIRECTION_LEFT</field><next>')
			f.write('<block type="ozobot_go_to_next_intersection" id="1"><next>')
		elif direction=="N":
			f.write('<block type="ozobot_choose_way_at_intersection" id="4"><field name="DIRECTION">DIRECTION_RIGHT</field><next>')
			f.write('<block type="ozobot_go_to_next_intersection" id="1"><next>')
		elif direction=="E":
			f.write('<block type="ozobot_choose_way_at_intersection" id="1"><field name="DIRECTION">DIRECTION_FORWARD</field><next>')
			f.write('<block type="ozobot_go_to_next_intersection" id="1"><next>')
		elif direction=="W":
			f.write('<block type="ozobot_rotate_dropdown_default_speed" id="tRPMaS;/{JKP(anEuJy[" x="65" y="160"><field name="ANGLE_DEG">-180</field><next>')
			f.write('<block type="ozobot_go_to_next_intersection" id="1"><next>')
			
		block.append('<next><block><next><block>')
		direction = "E"
		curr = path[node]

	elif path[node]-curr == -1:
		if direction=="S":
			f.write('<block type="ozobot_choose_way_at_intersection" id="4"><field name="DIRECTION">DIRECTION_RIGHT</field><next>')
			f.write('<block type="ozobot_go_to_next_intersection" id="1"><next>')
		elif direction=="N":
			f.write('<block type="ozobot_choose_way_at_intersection" id="2"><field name="DIRECTION">DIRECTION_LEFT</field><next>')
			f.write('<block type="ozobot_go_to_next_intersection" id="1"><next>')
		elif direction=="E":
			f.write('<block type="ozobot_rotate_dropdown_default_speed" id="tRPMaS;/{JKP(anEuJy[" x="65" y="160"><field name="ANGLE_DEG">-180</field><next>')
			f.write('<block type="ozobot_go_to_next_intersection" id="1"><next>')
		elif direction=="W":
			f.write('<block type="ozobot_choose_way_at_intersection" id="1"><field name="DIRECTION">DIRECTION_FORWARD</field><next>')
			f.write('<block type="ozobot_go_to_next_intersection" id="1"><next>')
			
		block.append('<next><block><next><block>')
		direction = "W"
		curr = path[node]

	elif path[node]-curr == 5:
		if direction=="S":
			f.write('<block type="ozobot_choose_way_at_intersection" id="1"><field name="DIRECTION">DIRECTION_FORWARD</field><next>')
			f.write('<block type="ozobot_go_to_next_intersection" id="1"><next>')
		elif direction=="N":
			f.write('<block type="ozobot_rotate_dropdown_default_speed" id="tRPMaS;/{JKP(anEuJy[" x="65" y="160"><field name="ANGLE_DEG">-180</field><next>')
			f.write('<block type="ozobot_go_to_next_intersection" id="1"><next>')
		elif direction=="E":
			f.write('<block type="ozobot_choose_way_at_intersection" id="4"><field name="DIRECTION">DIRECTION_RIGHT</field><next>')
			f.write('<block type="ozobot_go_to_next_intersection" id="1"><next>')
		elif direction=="W":
			f.write('<block type="ozobot_choose_way_at_intersection" id="2"><field name="DIRECTION">DIRECTION_LEFT</field><next>')
			f.write('<block type="ozobot_go_to_next_intersection" id="1"><next>')
			
		block.append('<next><block><next><block>')
		direction = "S"
		curr = path[node]

	elif path[node]-curr == -5:
		if direction=="S":
			f.write('<block type="ozobot_rotate_dropdown_default_speed" id="tRPMaS;/{JKP(anEuJy[" x="65" y="160"><field name="ANGLE_DEG">-180</field><next>')
			f.write('<block type="ozobot_go_to_next_intersection" id="1"><next>')
		elif direction=="N":
			f.write('<block type="ozobot_choose_way_at_intersection" id="1"><field name="DIRECTION">DIRECTION_FORWARD</field><next>')
			f.write('<block type="ozobot_go_to_next_intersection" id="1"><next>')
		elif direction=="E":
			f.write('<block type="ozobot_choose_way_at_intersection" id="2"><field name="DIRECTION">DIRECTION_LEFT</field><next>')
			f.write('<block type="ozobot_go_to_next_intersection" id="1"><next>')
		elif direction=="W":
			f.write('<block type="ozobot_choose_way_at_intersection" id="4"><field name="DIRECTION">DIRECTION_RIGHT</field><next>')
			f.write('<block type="ozobot_go_to_next_intersection" id="1"><next>')
			
		block.append('<next><block><next><block>')
		direction = "N"
		curr = path[node]

	elif path[node] == curr:
		f.write('<block type="system_delay" id="1"><value name="TIME_DELAY"><block type="math_number" id="1"><field name="NUM">100</field></block></value><next>')

	else: print('Error!!!!!!!!! -> wrong path at ', path[node])

# write close tabs
if direction == 'N':
	f.write('<block type="ozobot_choose_way_at_intersection" id="1"><field name="DIRECTION">DIRECTION_FORWARD</field><next>')
	f.write('<block type="ozobot_go_to_next_intersection" id="1"><block>')
elif direction == 'E':
	f.write('<block type="ozobot_choose_way_at_intersection" id="2"><field name="DIRECTION">DIRECTION_LEFT</field><next>')
	f.write('<block type="ozobot_go_to_next_intersection" id="1"><block>')
	block.append('<next><block>')
elif direction == 'W':
	f.write('<block type="ozobot_choose_way_at_intersection" id="4"><field name="DIRECTION">DIRECTION_RIGHT</field><next>')
	f.write('<block type="ozobot_go_to_next_intersection" id="1"><block>')
	block.append('<next><block>')

for b in block:
	f.write(b)

f.write('<next><block></xml>')
f.close()
