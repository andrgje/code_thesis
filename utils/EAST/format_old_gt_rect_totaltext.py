import os
from scipy.io import loadmat
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--data_path",help="path of folder containing ground truth", type = str)
parser.add_argument("--output_path", help="path of where to store new annotations", type=str)

args = parser.parse_args()

for f_in in os.listdir(args.data_path):
	filename=os.fsdecode(f_in)
	filepath=os.path.join(args.data_path,filename)
	file_id = int(filename.split('.')[0][11:])
	anno = loadmat(filepath)
	gt = anno['rectgt']
	print(gt)
	x = []
	y = []
	words = []
	for i in gt:
		x.append(i[1][0])
		y.append(i[3][0])
		words.append(i[4][0])

	f_out= open(args.output_path+'img_%d.txt'%(file_id),'w+')
		
	for k in range(len(x)):
		for x_cor,y_cor in zip(x[k],y[k]):
			f_out.write('%d,%d,'%(x_cor,y_cor))

		f_out.write(words[k]+'\n')

	f_out.close()

