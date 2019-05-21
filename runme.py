# -*- coding: utf-8 -*-

def haveSameLetters(srcm, norm):
	return (sorted(srcm) == sorted(norm))

def main():
	mgs_stop = "Πατήστε ENTER για να τερματίσετε το πρόγραμμα."
	msg_help = "Εισάγετε την ανακατεμένη λέξη. Το πρόγραμμα θα προσπαθήσει να βρεί τη λύση."
	msg_prompt = "> "
	words = file("dict.txt" , "r").read().split()

	print(mgs_stop)
	print(msg_help)
	scrambled = raw_input(msg_prompt)
	while scrambled != "" :
		answerlist = [normal for normal in words if len(normal) == len(scrambled) and haveSameLetters(scrambled,normal)]
		for (i, answer) in enumerate(answerlist): print("  " + str(i+1) + ". " + answer) 
		scrambled = raw_input(msg_prompt)

if __name__ == "__main__": main()
