## 问题描述
在查看pyskl仓库NTURGB+D [2D Skeleton]的时候发现，使用Cross Subject方式将NTU RGB+D数据集划分为训练集和测试集，遇到了缺失值
链接在下面
https://download.openmmlab.com/mmaction/pyskl/data/nturgbd/ntu60_hrnet.pkl

## 需求
split字段是字典类型，包含xsub_train键、xsub_val键、xview_train键、xview_val键

而xsub_train键对应的值发现查看列表长度length的时候遇到了缺失值，于是想把这些缺失值给找出来是哪些？

xsub_val键对应的值发现查看列表长度length的时候同样遇到了缺失值，于是想把这些缺失值给找出来是哪些？


## 解决方案

处理pkl.py就是来找这些缺失值是哪些的

## 附带需求
当然处理pkl.py还有一个功能是把xview_train键及其对应的值删除，把xview_val键及其对应的值删除。


