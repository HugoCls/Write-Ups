alphabet = "abcdefghijklmnopqrstuvwxyz_."

def new_chr(letter,k):
    return(alphabet[(alphabet.find(letter)+k) % len(alphabet)])

def reverse_embrouilleur(message,longueur_embrouilleur):
    new_message = ""
    for i in range(len(message)):
        old_str = message[i]
        decalage = i % longueur_embrouilleur + 1
        new_str = new_chr(old_str,- decalage)
        
        new_message += new_str
    return(new_message)

print(reverse_embrouilleur("ftqfuwjph.prvubfervvh",3))