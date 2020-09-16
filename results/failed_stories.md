## happy path 1 (C:\Users\JORGE~1.ALC\AppData\Local\Temp\tmpd3_pnrs1\be844250600b4b068fa1114e285c8911_conversation_tests.md)
* greet: hello there!   <!-- predicted: deny: hello there! -->
    - utter_greet   <!-- predicted: utter_happy -->
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_cumprimentar -->


## happy path 2 (C:\Users\JORGE~1.ALC\AppData\Local\Temp\tmpd3_pnrs1\be844250600b4b068fa1114e285c8911_conversation_tests.md)
* greet: hello there!   <!-- predicted: deny: hello there! -->
    - utter_greet   <!-- predicted: utter_happy -->
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_cumprimentar -->
* goodbye: bye-bye!   <!-- predicted: affirm: bye-bye! -->
    - utter_goodbye   <!-- predicted: utter_happy -->


## sad path 1 (C:\Users\JORGE~1.ALC\AppData\Local\Temp\tmpd3_pnrs1\be844250600b4b068fa1114e285c8911_conversation_tests.md)
* greet: hello   <!-- predicted: deny: hello -->
    - utter_greet   <!-- predicted: utter_happy -->
* mood_unhappy: not good
    - utter_cheer_up   <!-- predicted: utter_cumprimentar -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes
    - utter_happy


## sad path 2 (C:\Users\JORGE~1.ALC\AppData\Local\Temp\tmpd3_pnrs1\be844250600b4b068fa1114e285c8911_conversation_tests.md)
* greet: hello   <!-- predicted: deny: hello -->
    - utter_greet   <!-- predicted: utter_happy -->
* mood_unhappy: not good
    - utter_cheer_up   <!-- predicted: utter_cumprimentar -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really
    - utter_goodbye   <!-- predicted: utter_happy -->


## sad path 3 (C:\Users\JORGE~1.ALC\AppData\Local\Temp\tmpd3_pnrs1\be844250600b4b068fa1114e285c8911_conversation_tests.md)
* greet: hi   <!-- predicted: deny: hi -->
    - utter_greet   <!-- predicted: utter_cumprimentar -->
* mood_unhappy: very terrible
    - utter_cheer_up   <!-- predicted: utter_cumprimentar -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no
    - utter_goodbye   <!-- predicted: utter_happy -->


## say goodbye (C:\Users\JORGE~1.ALC\AppData\Local\Temp\tmpd3_pnrs1\be844250600b4b068fa1114e285c8911_conversation_tests.md)
* goodbye: bye-bye!   <!-- predicted: affirm: bye-bye! -->
    - utter_goodbye   <!-- predicted: utter_happy -->


## bot challenge (C:\Users\JORGE~1.ALC\AppData\Local\Temp\tmpd3_pnrs1\be844250600b4b068fa1114e285c8911_conversation_tests.md)
* bot_challenge: are you a bot?   <!-- predicted: mood_unhappy: are you a bot? -->
    - utter_iamabot   <!-- predicted: utter_cumprimentar -->


