import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--directory',type=str,required=True)

args=parser.parse_args()
directory=args.directory

for file in os.listdir(directory):
	filename = os.fsdecode(file)	
	if filename.endswith('.txt'):
		filepath = os.path.join(directory,filename)
		f = open(filepath,'r')	
		lines = f.readlines()
		coordinates=[]
		labels=[]
		
		for line in lines:
			line = line.split(', ')
			for i in range(4):
				coordinates.append(int(line[i]))
			labels.append(line[4])

		f.close()
		#For training: filepath = filepath.replace("gt","img")
		f=open(filepath,'w')
		counter = 0
		for i,label in enumerate(labels):
			x1 = coordinates[counter]
			x2 = coordinates[counter+2]
			y1 = coordinates[counter+1]
			y2 = coordinates[counter+3]
			f.write('%d,%d,%d,%d,%d,%d,%d,%d,'%(x1,y1,x2,y1,x2,y2,x1,y2))
			f.write(label[1:-2])
			if i<len(labels)-1:
				f.write('\n')
			counter+=4

		f.close()

#python multigpu_train.py --gpu_list=0 --input_size=512 --batch_size_per_gpu=14 --checkpoint_path=/tmp/east_icdar2015_resnet_v1_50_rbox/ --text_scale=512 --training_data_path=../Datasets/ICDAR2013/Training --geometry=RBOX --learning_rate=0.0001 --num_readers=24 --pretrained_model_path=./resnet_v1_50.ckpt
