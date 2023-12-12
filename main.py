import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the DataFrame
df_all_players = pd.DataFrame(columns=['PlayerName', 'Team', 'Nationality', 'Age', 'Height', 'PreferedFoot', 'Position', 'PlayerValue', 'TotalPlayed', 'Started', 'MinutePerGame', 'TeamOfTheWeek', 'Goals',
                                       'ExpectedGoals', 'ScoringFrequency', 'GoalsPerGame', 'ShotsPerGame',
                                       'ShotsOnTargetPerGame', 'BigChancesMissed', 'GoalConversion', 'FreeKickGoals',
                                       'FreeKickConversion', 'GoalsFromInsideTheBox', 'GoalsFromOutsideTheBox', 'HeadedGoals',
                                       'LeftFootGoals', 'RightFootGoals', 'PenaltyWon', 'Assists', 'ExpectedAssists', 'Touches',
                                       'BigChanceCreated', 'KeyPasses', 'AccuratePerGame', 'Acc.OwnHalf', 'Acc.opposition_half',
                                       'Acc.long_balls', 'Acc.chipped_passes', 'Acc.crosses', 'Interceptions_per_game', 'Tackles_per_game',
                                       'Possession won', 'Balls_recovered_per_game', 'Dribbled_past_per_game',
                                       'Clearances_per_game', 'Error_led_to_shot', 'ErrorLeadToShot', 'ErrorLedToGoal', 'PenaltiesCommited',
                                       'Yellow', 'Yellow-Red', 'Red-Cards'])

# Initialize the WebDriver
driver = webdriver.Chrome()

# Get the main page
driver.get("https://www.sofascore.com/team/football/galatasaray/3061")
time.sleep(5)

# Use find_elements instead of find_element to get a list of WebElements
urls = []

for i in range(1, 7):
    xpath = f'/html/body/div[1]/main/div[2]/div/div[2]/div[1]/div[5]/div[1]/div[3]/div[1]/div[2]/div[{i}]/a'
    link = driver.find_element(By.XPATH, xpath)
    urls.append(link.get_attribute("href"))

# Loop through player URLs
for url in urls:
    player_info = {}  # Initialize an empty dictionary for player information
    driver.get(url)
    time.sleep(5)

    # Extract player name
    player_info['PlayerName'] = driver.execute_script("return document.querySelector('h2.sc-jEACwC.iLVhST').innerText")

    # Extract team information
    player_info['Team'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/a/div/div/div[1]").text.strip()

    # Extract nationality
    player_info['Nationality'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div/span").text.strip()

    # Extract other information with try-except blocks
    try:
        player_info['Age'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]").text
    except:
        player_info['Age'] = '-'

    try:
        player_info['Height'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div[3]/div[2]").text
    except:
        player_info['Height'] = '-'

    try:
        player_info['PreferedFoot'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]").text
    except:
        player_info['PreferedFoot'] = '-'

    try:
        player_info['Position'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div[5]/div[2]").text
    except:
        player_info['Position'] = '-'

    try:
        # Extract PlayerValue and standardize the format
        player_value_element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[1]/div[2]/div[1]/div[3]/div/div[1]/div[2]")
        player_value_text = player_value_element.text
        if 'M' in player_value_text:
            player_info['PlayerValue'] = player_value_text
        else:
            player_info['PlayerValue'] = player_value_text + 'M €'
    except:
        player_info['PlayerValue'] = '-'

    try:
        total_played = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[1]/div[2]/div[1]/span[2]").text()
        player_info['TotalPlayed'] = int(total_played)
    except:
        player_info['TotalPlayed'] = '-'

    try:
        player_info['Started'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[1]/div[2]/div[2]/span[2]").text.strip()
    except:
        player_info['Started'] = '-'

    try:
        player_info['MinutePerGame'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[1]/div[2]/div[3]/span[2]").text.strip()
    except:
        player_info['MinutePerGame'] = '-'

    try:
        player_info['TeamOfTheWeek'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[1]/div[2]/div[4]/span[2]").text.strip()
    except:
        player_info['TeamOfTheWeek'] = '-'

    try:
        player_info['Goals'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[1]/span[2]").text.strip()
    except:
        player_info['Goals'] = '-'

    try:
        player_info['ExpectedGoals'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[2]/span[2]").text.strip()
    except:
        player_info['ExpectedGoals'] = '-'

    try:
        player_info['ScoringFrequency'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[3]/span[2]").text.strip()
    except:
        player_info['ScoringFrequency'] = '-'

    try:
        player_info['GoalsPerGame'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[4]/span[2]").text.strip()
    except:
        player_info['GoalsPerGame'] = '-'

    try:
        player_info['ShotsPerGame'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[5]/span[2]").text.strip()
    except:
        player_info['ShotsPerGame'] = '-'

    try:
        player_info['ShotsOnTargetPerGame'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[6]/span[2]").text.strip()
    except:
        player_info['ShotsOnTargetPerGame'] = '-'

    try:
        player_info['BigChancesMissed'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[7]/span[2]").text.strip()
    except:
        player_info['BigChancesMissed'] = '-'

    try:
        player_info['GoalConversion'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[8]/span[2]").text.strip()
    except:
        player_info['GoalConversion'] = '-'

    try:
        player_info['FreeKickGoals'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[9]/span[2]").text.strip()
    except:
        player_info['FreeKickGoals'] = '-'

    try:
        player_info['FreeKickConversion'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[10]/span[2]").text.strip()
    except:
        player_info['FreeKickConversion'] = '-'

    try:
        player_info['GoalsFromInsideTheBox'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[11]/span[2]").text.strip()
    except:
        player_info['GoalsFromInsideTheBox'] = '-'

    try:
        player_info['GoalsFromOutsideTheBox'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[12]/span[2]").text.strip()
    except:
        player_info['GoalsFromOutsideTheBox'] = '-'

    try:
        player_info['HeadedGoals'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[13]/span[2]").text.strip()
    except:
        player_info['HeadedGoals'] = '-'

    try:
        player_info['LeftFootGoals'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[14]/span[2]").text.strip()
    except:
        player_info['LeftFootGoals'] = '-'

    try:
        player_info['RightFootGoals'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[15]/span[2]").text.strip()
    except:
        player_info['RightFootGoals'] = '-'

    try:
        player_info['PenaltyWon'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[16]/span[2]").text.strip()
    except:
        player_info['PenaltyWon'] = '-'

    try:
        player_info['Assists'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[3]/div[2]/div[1]/span[2]").text.strip()
    except:
        player_info['Assists'] = '-'

    try:
        player_info['ExpectedAssists'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[3]/div[2]/div[2]/span[2]").text.strip()
    except:
        player_info['ExpectedAssists'] = '-'

    try:
        player_info['Touches'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[3]/div[2]/div[3]/span[2]").text.strip()
    except:
        player_info['Touches'] = '-'

    try:
        player_info['BigChanceCreated'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[3]/div[2]/div[4]/span[2]").text.strip()
    except:
        player_info['BigChanceCreated'] = '-'

    try:
        player_info['KeyPasses'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[3]/div[2]/div[5]/span[2]").text.strip()
    except:
        player_info['KeyPasses'] = '-'

    try:
        player_info['AccuratePerGame'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[3]/div[2]/div[6]/span[2]").text.strip()
    except:
        player_info['AccuratePerGame'] = '-'

    try:
        player_info['Acc.OwnHalf'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[3]/div[2]/div[7]/span[2]").text.strip()
    except:
        player_info['Acc.OwnHalf'] = '-'

    try:
        player_info['Acc.opposition_half'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[3]/div[2]/div[8]/span[2]").text.strip()
    except:
        player_info['Acc.opposition_half'] = '-'

    try:
        player_info['Acc.long_balls'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[3]/div[2]/div[9]/span[2]").text.strip()
    except:
        player_info['Acc.long_balls'] = '-'

    try:
        player_info['Acc.chipped_passes'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[3]/div[2]/div[10]/span[2]").text.strip()
    except:
        player_info['Acc.chipped_passes'] = '-'

    try:
        player_info['Acc.crosses'] = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div[5]/div[3]/div[2]/div[11]/span[2]").text.strip()
    except:
        player_info['Acc.crosses'] = '-'



    df_all_players = df_all_players._append(player_info, ignore_index=True)

# Reset the index to ensure it is unique
df_all_players.reset_index(drop=True, inplace=True)

# Close the WebDriver
driver.quit()

# Save the DataFrame to an Excel file
df_all_players.to_excel('data.xlsx', index=False)
