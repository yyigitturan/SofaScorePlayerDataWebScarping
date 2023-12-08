import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the DataFrame
df_all_players = pd.DataFrame(columns=['PlayerName', 'Team','Nationality', 'Age', 'Height', 'PreferedFoot', 'Position', 'PlayerValue', 'TotalPlayed', 'Started', 'MinutePerGame', 'TeamOfTheWeek', 'Goals',
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
    driver.get(url)
    time.sleep(5)

    # Extract player name using JavaScript to get innerText directly
    player_name_element = driver.execute_script("return document.querySelector('h2.sc-jEACwC.iLVhST').innerText")
    player_name = player_name_element.strip()

    # Append data to the DataFrame
    df_all_players = df_all_players._append({
        'PlayerName': player_name
    }, ignore_index=True)

# Reset the index to ensure it is unique
df_all_players.reset_index(drop=True, inplace=True)

# Close the WebDriver
driver.quit()

# Save the DataFrame to an Excel file
df_all_players.to_excel('data.xlsx', index=False)
