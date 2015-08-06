# -*- coding: utf-8 -*-

def haveSameLetters(dest , norm):
	
	dlst = list(dest)
	nlst = list(norm)
	dlst.sort()
	nlst.sort()

	for i in range(len(dlst)):
		if dlst[i] != nlst[i] :
			return False
	return True

def main():
	print("Πατήστε ENTER για να τερματίσετε το πρόγραμμα.")
	words = file("dict.txt" , "r").read().split()
	scrambled = raw_input("Εισάγεται την ανακατεμένη λέξη. Το πρόγραμμα θα προσπαθήσει να βρεί τη λύση: ")
	while scrambled != "" :
		answerlist = [normal for normal in words if len(normal) == len(scrambled) and haveSameLetters(scrambled,normal)]
		for answer in answerlist : print(answer) 
		scrambled = raw_input("Εισάγεται την ανακατεμένη λέξη. Το πρόγραμμα θα προσπαθήσει να βρεί τη λύση: ")

if __name__ == "__main__": main()
