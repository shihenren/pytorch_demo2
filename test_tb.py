from torch.utils.tensorboard import SummaryWriter
import os
import cv2


writer = SummaryWriter('logs')#实例化一个writer对象，指定存储路径为‘logs’
# img_path = 'data/train/ants_image/0013035.jpg'
# img = cv2.imread(img_path)
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# # print(img.shape)
# writer.add_image('ants1',img,1,dataformats='HWC')
# writer.close()

root_path = 'data/train/ants_image'
img_path = os.listdir(root_path) #列出文件夹下所有图片的名字

for i,img in enumerate(img_path):#i为枚举的索引，img为图片名
    path = os.path.join(root_path,img) #把文件夹路径和图片名拼起来就变成图片的完整路径
    print(path)
    if path[-4:] != '.jpg':#如果文件夹中有文件不是jpg形式的就跳过
        continue
    image = cv2.imread(path)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    writer.add_image(f"ants{i}",image,i,dataformats='HWC')

writer.close()