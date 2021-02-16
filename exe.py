import time
import schedule
import automata
import database
import java
import oSys
import topics

# automata
schedule.every().tuesday.at("09:31").do(automata.start)
schedule.every().thursday.at("09:29").do(automata.start)
# OS
schedule.every().tuesday.at("14:05").do(oSys.start)
schedule.every().thursday.at("13:59").do(oSys.start)
##


while True:
    schedule.run_pending()
    print("wait")
    time.sleep(180)

# Monday
# Tuesday
# Wednesday
# Thursday
# Friday
# Saturday
# Sunday
