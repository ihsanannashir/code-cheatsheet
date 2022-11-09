import os
import shutil
import fnmatch

original = os.path.expanduser("./emotion-dataset/angry")
target = os.path.expanduser("./anger/HI'")

# original = r'C:\Manners\D_Drive\Manners\SKRIPSI\Kode\archive\sad'
# target = r'C:\Manners\D_Drive\Manners\SKRIPSI\Kode\AudioWAV\HIGH'

pattern = 'HI'

src_files = os.listdir(original)

for file_name in src_files:
    if fnmatch.fnmatch(file_name,pattern)==True:
        full_file_name= os.path.join(original, file_name)

        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, target)
