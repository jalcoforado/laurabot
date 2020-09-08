## happy path 1 (C:\Users\Jorge\AppData\Local\Temp\tmpuo4vgpi1\bc395f70ee9045d7a32a69d7af5d96b2_conversation_tests.md)
* greet: hello there!   <!-- predicted: deny: hello there! -->
    - utter_greet   <!-- predicted: action_default_fallback -->
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_cheer_up -->


## happy path 2 (C:\Users\Jorge\AppData\Local\Temp\tmpuo4vgpi1\bc395f70ee9045d7a32a69d7af5d96b2_conversation_tests.md)
* greet: hello there!   <!-- predicted: deny: hello there! -->
    - utter_greet   <!-- predicted: action_default_fallback -->
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_cheer_up -->
* goodbye: bye-bye!   <!-- predicted: affirm: bye-bye! -->
    - utter_goodbye   <!-- predicted: action_default_fallback -->


## sad path 1 (C:\Users\Jorge\AppData\Local\Temp\tmpuo4vgpi1\bc395f70ee9045d7a32a69d7af5d96b2_conversation_tests.md)
* greet: hello   <!-- predicted: informar_nome: hello -->
    - utter_greet   <!-- predicted: utter_perguntar_ajuda -->
* mood_unhappy: not good   <!-- predicted: deny: not good -->
    - utter_cheer_up   <!-- predicted: action_default_fallback -->
    - utter_did_that_help
* affirm: yes
    - utter_happy


## sad path 2 (C:\Users\Jorge\AppData\Local\Temp\tmpuo4vgpi1\bc395f70ee9045d7a32a69d7af5d96b2_conversation_tests.md)
* greet: hello   <!-- predicted: informar_nome: hello -->
    - utter_greet   <!-- predicted: utter_perguntar_ajuda -->
* mood_unhappy: not good   <!-- predicted: deny: not good -->
    - utter_cheer_up   <!-- predicted: action_default_fallback -->
    - utter_did_that_help
* deny: not really
    - utter_goodbye   <!-- predicted: utter_despedir -->


## sad path 3 (C:\Users\Jorge\AppData\Local\Temp\tmpuo4vgpi1\bc395f70ee9045d7a32a69d7af5d96b2_conversation_tests.md)
* greet: hi   <!-- predicted: cumprimentar: hi -->
    - utter_greet   <!-- predicted: action_default_fallback -->
* mood_unhappy: very terrible
    - utter_cheer_up
    - utter_did_that_help
* deny: no
    - utter_goodbye   <!-- predicted: utter_despedir -->


## say goodbye (C:\Users\Jorge\AppData\Local\Temp\tmpuo4vgpi1\bc395f70ee9045d7a32a69d7af5d96b2_conversation_tests.md)
* goodbye: bye-bye!   <!-- predicted: affirm: bye-bye! -->
    - utter_goodbye   <!-- predicted: action_default_fallback -->


## bot challenge (C:\Users\Jorge\AppData\Local\Temp\tmpuo4vgpi1\bc395f70ee9045d7a32a69d7af5d96b2_conversation_tests.md)
* bot_challenge: are you a bot?   <!-- predicted: cumprimentar: are you a bot? -->
    - utter_iamabot   <!-- predicted: action_default_fallback -->


