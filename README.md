# teams-simulator
Simulate repeatedly joining a microsoft teams meeting as a guest

When you join a Teams meeting as a guest you are presented with a field to input your name. 
(Guest) is automatically appended to this name when you join. 
The next time you join a meeting, the name field will default to the last value, which if it contains spaces will put double quotes around the string. 
The time after that, the quotes will need to be escaped with backslashes. 
Then backslashes for the backslashes. 
Chaos ensues.

## Usage
1. Download teams-simulator.py
2. Do `python3 teams-simulator.py name number_of_times_to_join_meeting`
