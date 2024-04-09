import streamlit as st

"# Le boss de fin"
"Welcome tarde, donne la réponse à toutes les énigmes pour terminer"


""
""
""

"#### 'Donne moi le lui...'" #pulp fiction
if st.text_input("Réponse 2", help="pulp fiction").upper() == "YOAN" :
    st.success("✅ Niveau : Tarde en herbe")
else :
    st.stop()

""
""
""

"#### 'C'est à une demi heure d'ici. J'y suis dans'" #pulp fiction
if "DIX MINUTES" in st.text_input("Réponse 3", help="pulp fiction").upper() :
    st.success("✅ Niveau : Tarde junior")
else :
    st.stop()

""
""
""

"#### 'Jules c'est ' " #pulp fiction
rep = st.radio("Réponse 4", ["--", "un tarde", "un chanteur", "le noir"], horizontal=True, help="pulp fiction")
if rep == "le noir" :
    st.success("👍 Niveau : Tardinio")
elif rep == "un tarde" :
    "... ouais ca marche aussi."
    st.success("👍 Niveau : Tardinio")
else :
    st.stop()

st.image("img/jules_pulp.gif")

""
""
""

"#### 'Vincent c'est'" #pulp fiction
rep = st.radio("Réponse 5", ["--", "un tarde", "un chanteur", "le blanc"], horizontal=True, help="pulp fiction")
if rep == "le blanc" :
    st.success("👍 Niveau : Tardiflette")
elif rep == "un tarde" :
    "... ouais ca marche aussi."
    st.success("👍 Niveau : Tardiflette")
else :
    st.stop()

st.image("img/vincent_pulp.gif")


""
""
""

"#### 'Ah c'est par là la rentrée ? Ah merde.'" #135.3 db
if "SE FOUT DE MA GUEULE LUI" in st.text_input("Réponse 5", help="135.3 db").upper() :
    st.success("👏 Niveau : Ptitarde")
else :
    st.stop()

""
""
""

"#### 'Olivier !!'" #135.3db
if "TU VAS ME NIQUER LA BATTERIE" in st.text_input("Réponse 6", help="135.3 db").upper() :
    st.success("👏 Niveau :  Tarde")
else :
    st.stop()

st.image("img/olivier.gif")

""
""
""

"#### 'Il faut que tu les manges...' " #135.3db
if "tes pates" == st.radio("Réponse 7", ["--", "tes pates", "tes morts", "tes frites", "ton saumon vapeur sur son lit de courgette persillade"], horizontal=True, help="135.3 db") :
    st.success("🥳 Niveau : Grostardmorve")
else :
    st.stop()

""
""
""

"#### 'Vous etes plutot...' " #baptiste
if "petite ou grosse bagarre?" == st.radio("Réponse 8", ["--", "salé ou sucré?", "Messi ou Ronaldo?", "film ou série?", "petite ou grosse bagarre?"], horizontal=True, help="Baptiste") :
    st.success("🔥 Niveau : Tardos")
else :
    st.stop()

""
""
""

"#### 'Il faut faire super attention...' " #mousse
if "MOUSSE" in st.text_input("Réponse 9", help="Toniax").upper() :
    st.success("💣 Niveau : Tardissimo")
else :
    st.stop()

st.image("img/mousse.gif")

""
""
""

"#### 'C'est bien' " #pierrick
if "BLOUGE" in st.text_input("Réponse 10", help="Pierrick").upper() :
    st.success("💥 Niveau : Grand Tarde")
else :
    st.stop()

st.image("img/blouge.gif")

""
""
""

"#### 'Arabo?' " #oss117
if "MUSULMAN" in st.text_input("Réponse 11", help="oss117").upper() :
    st.success("💥💥💥 Niveau : Maxitarde")
else :
    st.stop()

""
""
""

"#### '(Projectile en direction de Pambrun)' " #oss117
if st.radio("Réponse 12", ["--", "Paf", "Boom", "PAAAAAAAAAAAAF... AAAAHHHHHHHH"], horizontal=True, help="Ti as vu le grani ?").upper() == "PAAAAAAAAAAAAF... AAAAHHHHHHHH" :
    st.success("💥💥💥 Niveau : Manu")
else :
    st.stop()

st.image("img/lancer.gif")

""
""
""

"#### 'Si ça va, dis moi un mot.'" #Pulp fiction
if st.text_input("Réponse 1", help="pulp fiction").upper() == "UN MOT" :
    st.success("💥💥💥 Niveau : Maxi Manu")
else :
    st.stop()

""
""
""

st.balloons()

if st.button("Excellent! Clique ici") :
    st.image("img/circle.jpg")

"#### Niveau 438 (Vidéo Jules ou Pierrick)"

""
""
""

"Rentrer la réponse à l'énigme principale"
