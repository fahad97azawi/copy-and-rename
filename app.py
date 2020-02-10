import os
import shutil

for i in range(13, 14):
    os.chdir('f:/Extra files/vape_cloud')

    for f in os.listdir():
        shutil.copy2(f'{os.getcwd()}/{f}', 'f:/Extra files/vape_cloud2', )

    for f in os.listdir():
        os.chdir('f:/Extra files/vape_cloud2')
        file_name = f'{i}-{f}'
        os.rename(f, file_name)
    
