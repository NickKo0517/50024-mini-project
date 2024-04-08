import re   #regex
import pandas as pd
from pathlib import Path

if __name__ == '__main__':
    pattern = "[^0-9]"      # class of all non-digit characters
    baseDirName = r"D:\Download\test_processed"
    baseDir = Path(baseDirName)
    filenames = [f.name for f in baseDir.iterdir() if f.is_file()]
    with open('test.csv', "w") as writer:
        writer.write('Id\n')
        for name in filenames:
            Id = re.sub(pattern, "", name)     #set non-digit parts to empty string
            writer.write(Id + '\n')
    
    df = pd.read_csv('test.csv')
    print(f'{len(df)} rows in test.csv')

