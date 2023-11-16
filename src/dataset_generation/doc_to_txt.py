import pypandoc
import os

# Example file:
dir = "../dataset/industry_collaborations"
for filename in os.listdir(dir):
    path = os.path.join(dir, filename)
    out_path = os.path.join(dir, filename).split(".docx")[0]
    output = pypandoc.convert_file(path, 'plain', outputfile=out_path+".txt")
    assert output == ""