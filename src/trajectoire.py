import numpy as np

CONSTANTE_GRAVITE = 9.81  # Accélération due à la gravité en m/s²

def calculer_trajectoire(vitesse_initiale, angle, temps_total, pas_de_temps):
    angle_rad = np.radians(angle)
    vitesse_x = vitesse_initiale * np.cos(angle_rad)
    vitesse_y = vitesse_initiale * np.sin(angle_rad)

    temps = np.arange(0, temps_total, pas_de_temps)
    x = []
    y = []

    # Calculer la position à chaque instant
    for t in temps:
        pos_x = vitesse_x * t
        pos_y = vitesse_y * t - 0.5 * CONSTANTE_GRAVITE * t**2  # 9.81 m/s² est l'accélération due à la gravité
        if pos_y < 0:  # Arrêter si la bille touche le sol
            break
        x.append(pos_x)
        y.append(pos_y)
    # Convertir les listes en tableaux numpy    
    x = np.array(x)
    y = np.array(y)
    # S'assurer que les tableaux ont la même longueur
    min_length = min(len(x), len(y))
    x = x[:min_length]
    y = y[:min_length]
    # Retourner les positions       
    return x, y
