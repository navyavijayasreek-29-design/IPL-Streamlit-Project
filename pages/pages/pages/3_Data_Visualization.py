import streamlit as st
import pandas as pd
import plotly.express as px

st.title("IPL Data Visualization")

df = pd.read_csv("IPL_2008_2026_Merged.csv")

# Matches by Season
st.header("Matches by Season")
matches_by_season = df.groupby("season").size()
st.bar_chart(matches_by_season)

# Wins by Team
st.header("Wins by Team")
wins_by_team = df["winner"].value_counts()
st.bar_chart(wins_by_team)

# Top Winning Teams
st.header("Top Winning Teams")
top_teams = wins_by_team.head(10).reset_index()
top_teams.columns = ["Team", "Wins"]

fig = px.bar(
    top_teams,
    x="Team",
    y="Wins",
    title="Top 10 Winning Teams"
)
st.plotly_chart(fig, use_container_width=True)

# Toss Decision
st.header("Toss Decision Distribution")
toss_data = df["toss_decision"].value_counts()

fig = px.pie(
    values=toss_data.values,
    names=toss_data.index,
    title="Toss Decisions"
)
st.plotly_chart(fig, use_container_width=True)

# Total Runs
st.header("Total Runs Distribution")

df["total_runs"] = (
    df["team1_runs"].fillna(0)
    + df["team2_runs"].fillna(0)
)

fig = px.histogram(
    df,
    x="total_runs",
    title="Distribution of Total Match Runs"
)
st.plotly_chart(fig, use_container_width=True)

# Scatter Plot
st.header("Team 1 Runs vs Team 2 Runs")

fig = px.scatter(
    df,
    x="team1_runs",
    y="team2_runs",
    title="Team 1 Runs vs Team 2 Runs"
)
st.plotly_chart(fig, use_container_width=True)
