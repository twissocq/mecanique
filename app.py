import streamlit as st
import matplotlib.pyplot as plt
import src.trajectoire as trajectoire

# Back-end: Fonction pour calculer la trajectoire
# Mémoire des lancers
if 'lancers' not in st.session_state:
    st.session_state.lancers = []

# Front-end: Interface utilisateur avec Streamlit
st.title("Simulation de la trajectoire d'un lancer de bille")

# Barre latérale pour les conditions initiales
with st.sidebar:
    st.header("Conditions initiales")
    vitesse_initiale = st.slider("Vitesse initiale (m/s)", 1, 50, 20)
    angle = st.slider("Angle de lancement (degrés)", 0, 90, 45)
    temps_total = st.slider("Temps total de simulation (s)", 1, 10, 4)
    # pas_de_temps = st.slider("Pas de temps (s)", 0.01, 0.1, 0.01, step=0.01)
    pas_de_temps = 0.01  # Valeur fixe pour le pas de temps
    if st.button("Lancer la simulation"):
        x, y = trajectoire.calculer_trajectoire(vitesse_initiale, angle, temps_total, pas_de_temps)
        st.session_state.lancers.append((x, y))

# Affichage des résultats sur le même graphique
if st.session_state.lancers:
    fig, ax = plt.subplots()
    for i, lancer in enumerate(st.session_state.lancers):
        ax.plot(lancer[0], lancer[1], label=f"Lancer {i+1}")

    ax.set_title("Trajectoires des lancers")
    ax.set_xlabel("Distance horizontale (m)")
    ax.set_ylabel("Hauteur (m)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
else:
    st.write("Aucun lancer effectué pour le moment.")