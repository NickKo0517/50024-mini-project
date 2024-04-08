import pandas as pd
import PIL.Image as Image
import cv2
from pathlib import Path



if __name__ == '__main__':
    train = pd.read_csv(r"valid_img_names.csv")
    category = pd.read_csv(r"D:\Download\category.csv")
    
    dir_name = r'D:\Download\train_processed\\'
    base_dir = Path(dir_name)

    with open(r"D:\Download\train_processed.csv", 'w') as writer:
        writer.write('label,file name\n')
        cnt: int = 0
        for i,img in enumerate(base_dir.iterdir()):
            if img.is_file():
                name = img.name.replace('gray_', '')
                print(name)
                celebrityName: str = train.loc[train['File Name'] == name]['Category'].values[0]
                label: str = str(
                    category.loc[category['Category'] == celebrityName]['Unnamed: 0'].values[0]
                )
                writer.write(label + ',' + name + '\n')
                cnt += 1
        print("write {} rows".format(cnt))

