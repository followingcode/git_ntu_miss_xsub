import pickle

pkl_file_path = 'ntu60_hrnet.pkl'
with open(pkl_file_path, 'rb') as file:
    pkl_data = pickle.load(file)

# 从 pkl 数据中获取 xsub_train 和 xsub_val 列表
xsub_train_list = pkl_data["split"]["xsub_train"]
xsub_val_list = pkl_data["split"]["xsub_val"]

# 从 txt 文件中读取所有文件路径，并提取文件名
txt_file_path = 'my_new_X-sub_content.txt'
with open(txt_file_path, 'r') as file:
    file_lines = file.readlines()

file_names = [line.strip().split('/')[-1].split('.')[0] for line in file_lines if 'Train' in line]

# 找出 file_names 中不存在于 xsub_train_list 的项
missing_files = [item for item in file_names if item not in xsub_train_list]

# 将不存在的项保存到新的 txt 文件中
missing_files_path = 'missing_files.txt'
with open(missing_files_path, 'w') as file:
    for item in missing_files:
        file.write(f"{item}\n")

# 从另一个 txt 文件中读取所有文件路径，并提取文件名
val_file_path = 'mymy.txt'
with open(val_file_path, 'r') as file:
    val_lines = file.readlines()

val_file_names = [line.strip().split('/')[-1].split('.')[0] for line in val_lines if 'Test' in line]

# 找出 val_file_names 中不存在于 xsub_val_list 的项
val_files = [item for item in val_file_names if item not in xsub_val_list]

# 将不存在的项保存到新的 txt 文件中
val_not_in_path = 'val_not_in.txt'
with open(val_not_in_path, 'w') as file:
    for item in val_files:
        file.write(f"{item}\n")


if "xview_train" in pkl_data["split"]:
    del pkl_data["split"]["xview_train"]
if "xview_val" in pkl_data["split"]:
    del pkl_data["split"]["xview_val"]

new_pkl_file_path = 'new_ntu60_hrnet_modified.pkl'
with open(new_pkl_file_path, 'wb') as file:
    pickle.dump(pkl_data, file)