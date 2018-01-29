Machine Learning Assignment 1 - Soccer Data
  - API: http://api.football-data.org/

# Install
**Build from source** :
  - clone https://github.com/DaljitSohi/SoccerData.git
  - cd SoccerData
  - Install 'runp' if not already installed:
    > sudo pip install runp

# Usage
  - **League Tables**:
      > runp soccerData.py leagueTable:_LeagueID_
      > - Example: runp soccerData.py leagueTable:PL
  - **Fixtures List**:
      > This output fixtures that have been played, and also the once that are yet to be played.
      > - runp soccerData.py  leagueTable:_LeagueID_
  - **Leagues**:
    - **League**          :        **League ID**
    - Seria A         :        SA
    - Premier League  :        PL
    - Ligue 1         :        Ligue1
    - Bundesliga 1    :        BL1
    
 # After printing data to the console, an CSV File is also made in the same directory as Script
  - **For League Tables**
    - File is named 'LeagueName'_Table.csv
  - **For Fixtures List**
    - File is named 'LeagueName'_FixtureList.csv
