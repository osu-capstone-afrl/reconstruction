
# DECIMATION PIPELINE
# Author: acbuynak
# Date:   2021/03/14

import os
import json
import subprocess
import numpy as np


pipeline = '/home/aims-zaphod/AA_AFRL/ImageProcessing/imageReduction.json'

directory_top   = '/home/aims-zaphod/Desktop/Photos/Set1/'
directory_input = directory_top + 'JPG_original'


counter=0
for filename in os.listdir(directory_input):
    if filename.endswith(".jpg") or filename.endswith(".JPG") or filename.endswith(".png") or filename.endswith(".PNG"):
        #print(os.path.join(directory_input, filename))
        counter+=1
        print(counter)

        photoNumber = filename[-8:-4]

        with open(pipeline, 'r') as jsonFile:
            data = json.load(jsonFile)

        data["0"]["FileName"] = str(os.path.join(directory_input, filename))

        # New Output Directories (filename already has extension type from original photo)
        data["4"]["FileName"] = directory_top + '/' + 'JPG_deci_half' + '/' + filename
        data["5"]["FileName"] = directory_top + '/' + 'JPF_deci_quarter' + '/' + filename
        data["6"]["FileName"] = directory_top + '/' + 'JPG_deci_eighth' + '/' + filename

        with open(pipeline, 'w') as jsonFile:
            json.dump(data, jsonFile)

        subprocess.call(["/opt/dream3d/bin/PipelineRunner", "-p", pipeline])

    else:
        continue