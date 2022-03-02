import pandas as pd
import argparse

parser=argparse.ArgumentParser()

parser.add_argument('--detections',help="pickle file with detections", type=str)
parser.add_argument('--output_path', help='path to store the formatted annotation files', type=str)

args=parser.parse_args()

res = pd.read_pickle(args.detections)

for i,img in enumerate(res):
    file_id=img['filename'].split('/')[-1].split('.')[0]
    f = open(args.output_path+'res_'+file_id+'.txt','w+')
    detections = img['boundary_result']
    for text in detections:
        for i,value in enumerate(text[:-1]):
                f.write('%d' %(int(value)))
                if(i<len(text)-2):
                    f.write(',')
        f.write('\n')