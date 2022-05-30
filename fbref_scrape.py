import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml

outfield_table_list = ["stats", "passing",
                       "shooting", "passing_types",
                       "gca", "defense",
                       "possession", "playingtime",
                       "misc"]

gk_table_list = ["keepers", "keepersadv"]


def get_fbref_player_data(stat):
    player_table = "https://fbref.com/en/comps/Big5/{stat}/players/Big-5-European-Leagues-Stats".format(stat=stat)
    scrape = requests.get(player_table).text
    soup = BeautifulSoup(scrape, 'lxml')
    table = soup.find("table", {"id": "stats_standard"})
    dataframe = pd.read_html(str(table))[0]
    dataframe.columns = dataframe.columns.map('|'.join).str.strip('|')
    dataframe = dataframe[dataframe["Unnamed: 0_level_0|Rk"].str.contains("Rk") == False]
    dataframe = dataframe.rename({'Unnamed: 1_level_0|Player': 'Player',
                                  'Unnamed: 2_level_0|Nation': 'Nation',
                                  'Unnamed: 3_level_0|Pos': 'Pos',
                                  'Unnamed: 4_level_0|Squad': 'Squad',
                                  'Unnamed: 5_level_0|Comp': 'Comp',
                                  'Unnamed: 6_level_0|Age': 'Age',
                                  'Unnamed: 7_level_0|Born': 'Born'}, axis=1)
    dataframe['Nation'] = dataframe['Nation'].str.split(' ', n=1).str.get(-1)
    dataframe['Comp'] = dataframe['Comp'].str.split(' ', n=1).str.get(-1)
    dataframe = dataframe[["Player", "Nation",
                           "Pos", "Squad",
                           "Comp", "Age",
                           "Born", "Playing Time|MP",
                           "Playing Time|Starts", "Playing Time|Min", "Playing Time|90s"]]
    return dataframe


stats_data = get_fbref_player_data("stats")


def get_fbref_match_data(stat):
    player_table = "https://fbref.com/en/comps/Big5/{stat}/players/Big-5-European-Leagues-Stats".format(stat=stat)
    scrape = requests.get(player_table).text
    soup = BeautifulSoup(scrape, 'lxml')
    table = soup.find("table", {"id": "stats_{stat}".format(stat=stat)})
    dataframe = pd.read_html(str(table))[0]
    dataframe.columns = dataframe.columns.map('|'.join).str.strip('|')
    dataframe = dataframe[dataframe["Unnamed: 0_level_0|Rk"].str.contains("Rk") == False]
    dataframe = dataframe.rename({'Unnamed: 1_level_0|Player': 'Player',
                                  'Unnamed: 4_level_0|Squad': 'Squad'}, axis=1).drop(
        dataframe.columns[[0, 2, 3, 5, 6, 7, 8, -1]], axis=1)
    return dataframe


def get_fbref_playing_time_data(stat):
    player_table = "https://fbref.com/en/comps/Big5/{stat}/players/Big-5-European-Leagues-Stats".format(stat=stat)
    scrape = requests.get(player_table).text
    soup = BeautifulSoup(scrape, 'lxml')
    table = soup.find("table", {"id": "stats_playing_time"})
    dataframe = pd.read_html(str(table))[0]
    dataframe.columns = dataframe.columns.map('|'.join).str.strip('|')
    dataframe = dataframe[dataframe["Unnamed: 0_level_0|Rk"].str.contains("Rk") == False]
    dataframe = dataframe.rename({'Unnamed: 1_level_0|Player': 'Player',
                                  'Unnamed: 4_level_0|Squad': 'Squad'}, axis=1).drop(
        dataframe.columns[[0, 2, 3, 5, 6, 7, 8, -1]], axis=1)
    return dataframe


shooting_data = get_fbref_match_data("shooting")
passing_data = get_fbref_match_data("passing")
possession_data = get_fbref_match_data("possession")
defense_data = get_fbref_match_data("defense")
passing_types_data = get_fbref_match_data("passing_types")
gca_data = get_fbref_match_data("gca")
misc_data = get_fbref_match_data("misc")
playing_time_data = get_fbref_playing_time_data("playingtime")
playing_time_data = playing_time_data.drop(labels=["Playing Time|Min", "Playing Time|90s"], axis=1)

merged_test = pd.merge(stats_data, shooting_data, on=["Player", "Squad"], how="left")

merged_test2 = pd.merge(merged_test, passing_data, on=["Player", "Squad"], how="left")

merged_test3 = pd.merge(merged_test2, passing_types_data, on=["Player", "Squad"], how="left")

merged_test4 = pd.merge(merged_test3, gca_data, on=["Player", "Squad"], how="left")

merged_test5 = pd.merge(merged_test4, possession_data, on=["Player", "Squad"], how="left")

merged_test6 = pd.merge(merged_test5, defense_data, on=["Player", "Squad"], how="left")

merged_test7 = pd.merge(merged_test6, playing_time_data, on=["Player", "Squad"], how="left")

merged_test8 = pd.merge(merged_test7, misc_data, on=["Player", "Squad"], how="left")



merged_test8["Expected|G-xG"] = merged_test8["Expected|G-xG"].str.replace("+", "")
merged_test8["Expected|np:G-xG"] = merged_test8["Expected|np:G-xG"].str.replace("+", "")
merged_test8["Unnamed: 25_level_0|A-xA"] = merged_test8["Unnamed: 25_level_0|A-xA"].str.replace("+", "")
merged_test8["Team Success|+/-"] = merged_test8["Team Success|+/-"].str.replace("+", "")
merged_test8["Team Success|+/-90"] = merged_test8["Team Success|+/-90"].str.replace("+", "")
merged_test8["Team Success|On-Off"] = merged_test8["Team Success|On-Off"].str.replace("+", "")
merged_test8["Team Success (xG)|xG+/-"] = merged_test8["Team Success (xG)|xG+/-"].str.replace("+", "")
merged_test8["Team Success (xG)|xG+/-90"] = merged_test8["Team Success (xG)|xG+/-90"].str.replace("+", "")
merged_test8["Team Success (xG)|On-Off"] = merged_test8["Team Success (xG)|On-Off"].str.replace("+", "")