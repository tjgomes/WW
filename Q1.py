import os.path


file_path = 'C:\Users\Home\Documents\dictionary.txt'


def doesFileExist(pathToFile):
    
    
	if (os.path.isfile(pathToFile)) :
        
		print "File is found and file path is " + pathToFile
    
	else :

        	print "File is not found"

doesFileExist(file_path)



dict = {'Apple': ['a fruit', 'a tech firm'],

        'Table': ['an object', 'contains rows and columns when used in context of computers'],

        'Orange': ['a fruit']
}



for x, y in dict.items():
  print(x, y)
