import os
import pandas as pd
import hashlib
import magic
import mimetypes

# specify the directory path where the files are located
dir_path = './Dokaz'

# create an empty list to store the file names
file_names = []
extensions = []
md5s=[]
sha1s=[]
sha256s=[]
magic_numbers=[]
extension_matches=[]

mag_obj=magic.Magic(mime=True)
# iterate through all files in the directory
for file in os.listdir(dir_path):
    # check if the file is a regular file (i.e., not a directory)
    if os.path.isfile(os.path.join(dir_path, file)):
        # if so, add the file name to the list
        name, exts=os.path.splitext(file)
        file_names.append(name)
        extensions.append(exts)

        with open(dir_path+"/"+name+exts, "rb") as f:
            data=f.read()

            md5s.append(hashlib.md5(data).hexdigest())
            sha1s.append(hashlib.sha1(data).hexdigest())
            sha256s.append(hashlib.sha256(data).hexdigest())
        magic_numbers.append(mag_obj.from_file(os.path.join(dir_path, file)))

        if exts.lower() == '':
            extension_matches.append(False)
        elif mimetypes.guess_type('test'+exts.lower())[0] in magic_numbers[-1].lower():
            extension_matches.append(True)
        else:
            extension_matches.append(False)

# create a Pandas dataframe with the file names
df = pd.DataFrame({'file_name': file_names, "extensions":extensions, "md5":md5s, "sha1":sha1s, "sha256":sha256s, "magic_numbers":magic_numbers, "extension_matches":extension_matches})

# print the dataframe
print(df)