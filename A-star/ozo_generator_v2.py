# Team2: Yuu Sakaguchi, Felipe Vianna, Chembrolu Surya
import numpy as np
import pandas as pd

# Given a sequence of a path, generates into Ozocode in XML.

# Path
PATH = [[1,2,7,12,12,12,12,12,13,18,23,23,23,23,23,23,23,18,19,19,19,19,19,19,19,19,14,9,4,5],
		[1,6,11,16,17,18,19,19,19,19,19,19,19,19,14,13,12,12,12,12,12,13,18,23,23,23,23,23,23,23,18,13,8,3,4,5],
		[1,1,1,1,2,7,7,7,7,7,12,12,12,12,12,17,17,17,17,17,18,17,17,17,17,17,18,18,19,19,19,19,19,19,19,19,18,23,23,23,23,23,23,23,18,13,8,3,4,5]]

# Compute who reaches the goal first, second and third.
goal_order=[]
path1_len = len(PATH[0])
path2_len = len(PATH[1])+1
path3_len = len(PATH[2])+2
goals = [path1_len, path2_len, path3_len]

goal_order.append(goals.index(min(goals)))
goals[goals.index(min(goals))] = -1
goal_order.append(goals.index(max(goals)))
if 0 not in goal_order:
	second = 0
elif 1 not in goal_order:
	second = 1
else:
	second = 2
goal_order.insert(1, second)


def forward():
	f.write('<block type="ozobot_choose_way_at_intersection" id="1"><field name="DIRECTION">DIRECTION_FORWARD</field><next>')
	f.write('<block type="ozobot_go_to_next_intersection" id="1"><next>')

def backward():
	f.write('<block type="ozobot_rotate_dropdown_default_speed" id="tRPMaS;/{JKP(anEuJy[" x="65" y="160"><field name="ANGLE_DEG">-180</field><next>')
	f.write('<block type="ozobot_go_to_next_intersection" id="1"><next>')

def left():
	f.write('<block type="ozobot_choose_way_at_intersection" id="2"><field name="DIRECTION">DIRECTION_LEFT</field><next>')
	f.write('<block type="ozobot_go_to_next_intersection" id="1"><next>')

def right():
	f.write('<block type="ozobot_choose_way_at_intersection" id="4"><field name="DIRECTION">DIRECTION_RIGHT</field><next>')
	f.write('<block type="ozobot_go_to_next_intersection" id="1"><next>')




i = 0
for path in PATH:

	print("PATH"+str(i+1)+": ", path)

	# Generate XML
	f = open('ozocode'+str(i+1)+'.txt', "w", encoding='UTF-8')
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

	# Start
	if i == 1:
		f.write('<block type="system_delay" id="1"><value name="TIME_DELAY"><block type="math_number" id="1"><field name="NUM">100</field></block></value><next>')
		forward()
	elif i == 2:
		f.write('<block type="system_delay" id="1"><value name="TIME_DELAY"><block type="math_number" id="1"><field name="NUM">100</field></block></value><next>')
		forward()
		f.write('<block type="system_delay" id="1"><value name="TIME_DELAY"><block type="math_number" id="1"><field name="NUM">100</field></block></value><next>')
		forward()


	for node in range(1,len(path)):
		#print(path[node])

		if path[node]-curr == 1:
			if direction=="S":
				left()
			elif direction=="N":
				right()
			elif direction=="E":
				forward()
			elif direction=="W":
				backward()
				
			block.append('<next><block><next><block>')
			direction = "E"
			curr = path[node]

		elif path[node]-curr == -1:
			if direction=="S":
				right()
			elif direction=="N":
				left()
			elif direction=="E":
				backward()
			elif direction=="W":
				forward()
				
			block.append('<next><block><next><block>')
			direction = "W"
			curr = path[node]

		elif path[node]-curr == 5:
			if direction=="S":
				forward()
			elif direction=="N":
				backward()
			elif direction=="E":
				right()
			elif direction=="W":
				left()
				
			block.append('<next><block><next><block>')
			direction = "S"
			curr = path[node]

		elif path[node]-curr == -5:
			if direction=="S":
				backward()
			elif direction=="N":
				forward()
			elif direction=="E":
				left()
			elif direction=="W":
				right()
				
			block.append('<next><block><next><block>')
			direction = "N"
			curr = path[node]

		elif path[node] == curr:
			f.write('<block type="system_delay" id="1"><value name="TIME_DELAY"><block type="math_number" id="1"><field name="NUM">100</field></block></value><next>')

		else: print('Error!!!!!!!!! -> wrong path at ', path[node])


	goal = goal_order.index(i)
	# Goal
	if goal == 0:
		if direction == 'N':
			f.write('<block type="ozobot_choose_way_at_intersection" id="1"><field name="DIRECTION">DIRECTION_FORWARD</field><next>')
			f.write('<block type="system_move" id="~Xhsa`),|Ea.ZhpG4?#f" x="185" y="131"><value name="DISTANCE_MM"><block type="math_number" id="(#m?(#;6W8yoe}/yr}1g"> \
					<field name="NUM">85</field></block></value><value name="SPEED_MMPS"><block type="math_number" id="W1ZUdawo^nXzDz_D}uRq"> \
					<field name="NUM">127</field></block></value></block>')
			block.append('<next><block>')
		elif direction == 'E':
			f.write('<block type="ozobot_rotate_dropdown_default_speed" id="=M,x]x04(mK!T?i+=;Hh" x="213" y="206"><field name="ANGLE_DEG">90</field><next>')
			f.write('<block type="system_move" id="~Xhsa`),|Ea.ZhpG4?#f" x="185" y="131"><value name="DISTANCE_MM"><block type="math_number" id="(#m?(#;6W8yoe}/yr}1g"> \
					<field name="NUM">85</field></block></value><value name="SPEED_MMPS"><block type="math_number" id="W1ZUdawo^nXzDz_D}uRq"> \
					<field name="NUM">127</field></block></value></block>')
			block.append('<next><block>')
		elif direction == 'W':
			f.write('<block type="ozobot_choose_way_at_intersection" id="4"><field name="DIRECTION">DIRECTION_RIGHT</field><next>')
			f.write('<block type="system_move" id="~Xhsa`),|Ea.ZhpG4?#f" x="185" y="131"><value name="DISTANCE_MM"><block type="math_number" id="(#m?(#;6W8yoe}/yr}1g"> \
					<field name="NUM">85</field></block></value><value name="SPEED_MMPS"><block type="math_number" id="W1ZUdawo^nXzDz_D}uRq"> \
					<field name="NUM">127</field></block></value></block>')
			block.append('<next><block>')
	elif goal == 1:
		if direction == 'N':
			f.write('<block type="ozobot_choose_way_at_intersection" id="1"><field name="DIRECTION">DIRECTION_FORWARD</field><next>')
			f.write('<block type="system_move" id="~Xhsa`),|Ea.ZhpG4?#f" x="185" y="131"><value name="DISTANCE_MM"><block type="math_number" id="(#m?(#;6W8yoe}/yr}1g"> \
					<field name="NUM">50</field></block></value><value name="SPEED_MMPS"><block type="math_number" id="W1ZUdawo^nXzDz_D}uRq"> \
					<field name="NUM">127</field></block></value></block>')
			block.append('<next><block>')
		elif direction == 'E':
			f.write('<block type="ozobot_rotate_dropdown_default_speed" id="=M,x]x04(mK!T?i+=;Hh" x="213" y="206"><field name="ANGLE_DEG">90</field><next>')
			f.write('<block type="system_move" id="~Xhsa`),|Ea.ZhpG4?#f" x="185" y="131"><value name="DISTANCE_MM"><block type="math_number" id="(#m?(#;6W8yoe}/yr}1g"> \
					<field name="NUM">50</field></block></value><value name="SPEED_MMPS"><block type="math_number" id="W1ZUdawo^nXzDz_D}uRq"> \
					<field name="NUM">127</field></block></value></block>')
			block.append('<next><block>')
		elif direction == 'W':
			f.write('<block type="ozobot_choose_way_at_intersection" id="4"><field name="DIRECTION">DIRECTION_RIGHT</field><next>')
			f.write('<block type="system_move" id="~Xhsa`),|Ea.ZhpG4?#f" x="185" y="131"><value name="DISTANCE_MM"><block type="math_number" id="(#m?(#;6W8yoe}/yr}1g"> \
					<field name="NUM">50</field></block></value><value name="SPEED_MMPS"><block type="math_number" id="W1ZUdawo^nXzDz_D}uRq"> \
					<field name="NUM">127</field></block></value></block>')
			block.append('<next><block>')
	elif goal == 2:
		if direction == 'N':
			f.write('<block type="ozobot_choose_way_at_intersection" id="1"><field name="DIRECTION">DIRECTION_FORWARD</field><next>')
			f.write('<block type="system_move" id="~Xhsa`),|Ea.ZhpG4?#f" x="185" y="131"><value name="DISTANCE_MM"><block type="math_number" id="(#m?(#;6W8yoe}/yr}1g"> \
					<field name="NUM">15</field></block></value><value name="SPEED_MMPS"><block type="math_number" id="W1ZUdawo^nXzDz_D}uRq"> \
					<field name="NUM">127</field></block></value></block>')
			block.append('<next><block>')
		elif direction == 'E':
			f.write('<block type="ozobot_rotate_dropdown_default_speed" id="=M,x]x04(mK!T?i+=;Hh" x="213" y="206"><field name="ANGLE_DEG">90</field><next>')
			f.write('<block type="system_move" id="~Xhsa`),|Ea.ZhpG4?#f" x="185" y="131"><value name="DISTANCE_MM"><block type="math_number" id="(#m?(#;6W8yoe}/yr}1g"> \
					<field name="NUM">15</field></block></value><value name="SPEED_MMPS"><block type="math_number" id="W1ZUdawo^nXzDz_D}uRq"> \
					<field name="NUM">127</field></block></value></block>')
			block.append('<next><block>')
		elif direction == 'W':
			f.write('<block type="ozobot_choose_way_at_intersection" id="4"><field name="DIRECTION">DIRECTION_RIGHT</field><next>')
			f.write('<block type="system_move" id="~Xhsa`),|Ea.ZhpG4?#f" x="185" y="131"><value name="DISTANCE_MM"><block type="math_number" id="(#m?(#;6W8yoe}/yr}1g"> \
					<field name="NUM">15</field></block></value><value name="SPEED_MMPS"><block type="math_number" id="W1ZUdawo^nXzDz_D}uRq"> \
					<field name="NUM">127</field></block></value></block>')
			block.append('<next><block>')


	

	for b in block:
		f.write(b)

	f.write('<next><block></xml>')
	f.close()
	i += 1