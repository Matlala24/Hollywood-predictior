
import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Hollywoodbets Predictor", layout="centered")

st.title("🎯 Hollywoodbets Prediction Robot")
st.markdown("Predict match or race outcomes based on basic logic. (Model-ready template)")

sport = st.selectbox("Choose a sport", ["Soccer", "Horse Racing"])

if sport == "Soccer":
    st.subheader("⚽ Soccer Match Prediction")
    home_team = st.text_input("Home Team", "Kaizer Chiefs")
    away_team = st.text_input("Away Team", "Orlando Pirates")

    if st.button("Predict Result"):
        result = random.choice(["Home Win", "Draw", "Away Win"])
        home_score = random.randint(0, 3)
        away_score = random.randint(0, 3)

        st.success(f"Prediction: **{result}**")
        st.info(f"Scoreline: {home_team} {home_score} - {away_score} {away_team}")

elif sport == "Horse Racing":
    st.subheader("🏇 Horse Racing Winner Prediction")
    race_name = st.text_input("Race Name", "Greyville Race 5")
    horses = st.text_area("Enter horse names (one per line)", "Thunderbolt\nWind Chaser\nDark Knight")

    if st.button("Predict Winner"):
        horse_list = horses.strip().split("\n")
        winner = random.choice(horse_list)
        st.success(f"Predicted Winner: **{winner}**")
