
# Background Mask PIPELINE Runner for Dream3D
# Author: acbuynak
# Date:   2021/03/18

import os
import json
import subprocess
import numpy as np


pipeline = '/home/user/YOUR/WORKSPACE/PATH/mask_first_pass.json'

directory_top   = '/home/user/YOUR/WORKSPACE/PATH/HERE/'
directory_input = directory_top + 'Original'


counter=0
for filename in os.listdir(directory_input):
    if filename.endswith(".jpg") or filename.endswith(".JPG") or filename.endswith(".png") or filename.endswith(".PNG"):
        #print(os.path.join(directory_input, filename))
        counter+=1
        print(counter)

        photoNumber = filename[-8:-4]

        with open(pipeline, 'r') as jsonFile:
            data = json.load(jsonFile)

        # Input File
        data["00"]["FileName"] = str(os.path.join(directory_input, filename))

        # New Output Directories (filename already has extension type from original photo)
        data["16"]["FileName"] = directory_top + '/' + 'Original_Masked_otsu' + '/' + filename

        # Debugging Outputs (overwirtes same files)
        data["15"]["FileName"] = directory_top + '/' + 'DebugPipeline/edgeFilter_mask.dream3d'
        data["17"]["FileName"] = directory_top + '/' + 'DebugPipeline/test_flagged.JPG'

        with open(pipeline, 'w') as jsonFile:
            json.dump(data, jsonFile, indent=4)

        subprocess.call(["/opt/dream3d/bin/PipelineRunner", "-p", pipeline])

    else:
        continue