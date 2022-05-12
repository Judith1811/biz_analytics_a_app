import streamlit as st

st.title("Historische Wetterdaten")
st.caption("Autorin: Judith Paaßen")

st.subheader("Finde heraus, wie lange die Sonne am Tag deiner Geburt in Deutschland schien.")
#%%
import pandas as pd
df = pd.read_excel('weather_dus.xls')
df.set_index('MESS_DATUM', inplace=True)
def model(date):
    result = df.loc[date,'SDK']*60
    return result
date = st.number_input('Trage hier dein Geburtsdatum in folgendem Format ein: JJJJMMDD', value=19700101, min_value=19700101, max_value=20181231)
prediction = model(date)
prediction_rounded = round(prediction)
st.subheader("An deinem Geburtstag schien die Sonne")
st.subheader(prediction_rounded)
st.subheader("Minuten.")

#%%
from PIL import Image
image = Image.open('Himmel.jpg')

st.image(image)

#%%
st.subheader("Über das Modell und die Daten")
"Das Modell ist gültig für Geburtstage vom 01.01.1970 bis zum 31.12.2018."
"Die Wetterdaten stammen aus folgender Quelle des deutschen Wetterdienstes: https://cdc.dwd.de/portal/"
"Das Bild entstammt folgender Quelle: https://www.pexels.com/de-de/@pixabay"
"Kontakt: judith.paassen@study.hs-duesseldorf.de"
