使用Cross Subject方式划分NTU RGB+D数据集遇到的缺失值，这个是在查看pyskl仓库NTURGB+D [2D Skeleton]的时候发现的

https://download.openmmlab.com/mmaction/pyskl/data/nturgbd/ntu60_hrnet.pkl


split字段是字典类型，包含xsub_train键、xsub_val键、xview_train键、xview_val键

而xsub_train键对应的值发现查看列表长度length的时候遇到了缺失值，于是想把这些缺失值给找出来是哪些？

xsub_val键对应的值发现查看列表长度length的时候同样遇到了缺失值，于是想把这些缺失值给找出来是哪些？

处理pkl这个代码就是来找这些缺失值是哪些的


当然处理pkl这个代码还有一个功能是把xview_train键及其对应的值删除，把xview_val键及其对应的值删除。

### 注意这里的xsub数据集的list列表里面的Train路径和Test路径是已经处理过缺失值之后的结果
