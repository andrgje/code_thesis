from scipy.io import loadmat
import numpy as np
import argparse
import os
import cv2
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()

parser.add_argument("--data_path",help="path of folder containing ground truth", type = str)
parser.add_argument("--output_path", help="path of where to store new annotations", type=str)

args = parser.parse_args()

for f_in in os.listdir(args.data_path):
	filename=os.fsdecode(f_in)
	filepath=os.path.join(args.data_path,filename)
	file_id = int(filename.split('.')[0][6:])
	anno = loadmat(filepath)
	gt = anno['gt']
	x = []
	y = []
	words = []
	for i in gt:
		x.append(i[1][0])
		y.append(i[3][0])
		words.append(i[4][0])

	f_out= open(args.output_path+'img_%d.txt'%(file_id),'w+')
		
	for k in range(len(x)):
			x_points = x[k]
			y_points = y[k]
		
			points = np.column_stack((x_points,y_points))
			points = points.astype(np.int32)
			rect = cv2.minAreaRect(points)
			box = np.int0(cv2.boxPoints(rect))
			for cor in box:
				if cor[0]<0:
					cor[0]=0
				if cor[1]<0:
					cor[1]=0
				f_out.write('%d,%d,'%(cor[0],cor[1]))
			
			f_out.write(words[k]+'\n')

	f_out.close()

#rename images	
#for f in *.jpg;do mv "$f" "${f:0:3}_${f:3}" ; doneD
