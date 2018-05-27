#ex: ./rename.py ./Snowdrop

import os, glob
import sys

directory = sys.argv[1]
pattern = r'*.jpg'

i=0
for pathAndFilename in glob.iglob(os.path.join(directory, pattern)):
	i = i + 1
	title, ext = os.path.splitext(os.path.basename(pathAndFilename))
	os.rename(pathAndFilename, 
		os.path.join(directory, 'image_' + str(i) + ext))