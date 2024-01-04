import jwt
import datetime

def create_jwt(username, role, secret_key="hello"):
    # Création des données à inclure dans le JWT (payload)
    payload = {
        "username": "votre_nom_utilisateur",
        "role": "votre_role",
        "iat": datetime.datetime.utcnow(),  # Horodatage de création du JWT
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Horodatage d'expiration (1 heure après la création)
    }

    # Génération du JWT
    jwt_token = jwt.encode(payload, secret_key, algorithm="HS256")

    print("JWT généré :", jwt_token)
    
    return(jwt_token)

# Fonction pour vérifier la validité du JWT
def is_valid_jwt(jwt_token, secret_key):
    """
    # Exemple d'utilisation
    jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InZvdHJlX25vbV91dGlsaXNhdGV1ciIsInJvbGUiOiJ2b3RyZV9yb2xlIiwiaWF0IjoxNjkwNDQ3MjMzLCJleHAiOjE2OTA0NTA4MzN9.fUJdXleq0IWH_26SO_CIlComVxMBCA5aYZyclXGM4S0"
    secret_key = "hello"

    result = is_valid_jwt(jwt_token, secret_key)
    """
    try:
        # Vérifie la signature du JWT en utilisant la clé secrète
        decoded_token = jwt.decode(jwt_token, secret_key, algorithms=['HS256'])
        
        print("Le JWT est valide.")
        print("Contenu du JWT décodé :", decoded_token)
        return decoded_token  # Si la vérification réussit, renvoie le contenu du JWT décodé
    
    except jwt.ExpiredSignatureError:
        # Le JWT a expiré
        print("Le JWT a expiré.")
        return False
    
    except jwt.InvalidTokenError:
        # Le JWT est invalide ou altéré
        print("Le JWT est invalide.")
        return False