from pwn import xor
## Détermination de la clé grace au début "crypto{" que l'on connait déjà
message = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
 
result = xor(message[:7], "crypto{")

message = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

## Calcul final
key = "myXORkey"

#complete_key = (partial_key * (len(message)//len(partial_key)+1))[:len(message)]

#print(complete_key)
# Le calcul avec une copie infinie de la clé se fait automatiquement

print(xor(message,key))