# Chaîne hexadécimale donnée
hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

# Convertir la chaîne hexadécimale en bytes
data = bytes.fromhex(hex_string)

# Fonction pour décoder avec une clé XOR
def xor_decrypt(data, key):
    return bytes([byte ^ key for byte in data])

# Essayer toutes les valeurs possibles de clé (0x00 à 0xFF)
for key in range(256):
    decrypted_data = xor_decrypt(data, key)
    # Convertir les données décryptées en chaîne de caractères
    decrypted_str = decrypted_data.decode('utf-8', errors='ignore')
    # Afficher le résultat si cela semble être du texte lisible
    if all(32 <= byte <= 126 or byte == 10 or byte == 13 for byte in decrypted_data):
        print(f"Clé : {key}, Message : {decrypted_str}")
