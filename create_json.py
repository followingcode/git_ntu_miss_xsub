import os
import decord
import json
import re

def writeJson(path_train, jsonpath):
    output_list = []
    trainfile_list = os.listdir(path_train)
    for train_name in trainfile_list:
        train_dict = {}
        sp = train_name.split('A')
        train_dict['vid_name'] = train_name.replace('.mp4', '')
        action_id = re.findall(r'\d+', sp[1])
        if action_id:
            action_id = int(action_id[0])
            # 在这里添加标签转换的逻辑
            train_dict['label'] = action_id - 1
        else:
            train_dict['label'] = None
        train_dict['start_frame'] = 0

        video_path = os.path.join(path_train, train_name)
        vid = decord.VideoReader(video_path)
        train_dict['end_frame'] = len(vid)
        output_list.append(train_dict.copy())

    # 对 output_list 进行排序
    output_list.sort(key=lambda x: x['vid_name'])

    # print(output_list)
    # print("OK")

    with open(jsonpath, 'w', encoding='utf-8') as outfile:
        json.dump(output_list, outfile)

writeJson(r'/root/autodl-tmp/Cross-Subject/Train', '/root/pyskl/until/ntu_train.json')
writeJson(r'/root/autodl-tmp/Cross-Subject/Test', '/root/pyskl/until/ntu_test.json')