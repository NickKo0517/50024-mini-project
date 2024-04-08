import pandas as pd

valid_img_names = pd.read_csv('valid_img_names.csv')['File Name'].values
train           = pd.read_csv(r"D:\Download\train.csv")
labels          = pd.read_csv(r"D:\Download\category.csv")

print(len(valid_img_names))
print(valid_img_names[:3])

with open('train_processed.csv', 'w') as writer:
    writer.write('File Name, Label\n')
    for name in valid_img_names:
        celebrityName: str = train.loc[train['File Name'] == name]['Category'].values[0]
        label: str = str(
            labels.loc[labels['Category'] == celebrityName]['Unnamed: 0'].values[0]
        )
        writer.write(name + ',' + label + '\n')



