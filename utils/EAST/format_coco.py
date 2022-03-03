import os
import argparse
import json
import ast

parser = argparse.ArgumentParser()

parser.add_argument('--anno_file', help="json file with gt for all images in set.", type=str)
parser.add_argument('--output_path', help="path to output folder", type=str)

args = parser.parse_args()

filepath = args.anno_file
output_path = args.output_path
f = open(filepath)


data = json.load(f)
f.close()

for img_id in data['imgs']:
    anns = data['imgToAnns'][str(img_id)]
    filename = 'img_'+img_id+'.txt'
    path = os.path.join(output_path,filename)
    f = open(path,'w+')
    for ann_id in anns:
        boundary = data['anns'][str(ann_id)]['mask']

        if data['anns'][str(ann_id)]['legibility']=='illegible':
            text = '###'
        else:
            text = data['anns'][str(ann_id)]['utf8_string']

        for nr in boundary:
            f.write('%d,'%nr)

        f.write(text+'\n')

    f.close()