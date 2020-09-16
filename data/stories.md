## caminho Prefeito
* cumprimentar
  - utter_cumprimentar 
* informar_nome{"nome": "jorge alberto"}
  - utter_perguntar_ajuda 
* nome_prefeito{"cidade":"São Paulo"}
  - action_get_prefeito 
  - utter_nomeprefeito
* vice_prefeito
  - utter_viceprefeito 
* affirm
  - utter_happy
  - utter_despedir


## caminho Governador
* cumprimentar
  - utter_cumprimentar 
* informar_nome{"nome": "jorge alberto"}
  - utter_perguntar_ajuda 
* nome_governador{"estado":"São Paulo"}
  - action_get_governador 
  - utter_nomegovernador
* vice_governador
  - utter_vicegovernador
* affirm
  - utter_happy
  - utter_despedir  

<!-- ## Procurando Serviços
* cumprimentar
  - utter_cumprimentar
* informar_nome{"nome": "jorge"}
  - slot{"nome": "jorge"}
  - utter_perguntar_ajuda  
* procurar_servicos
  - utter_perguntar_grupo_servico
  - utter_listar_grupos  
  - action_get_grupo_servico  -->

* affirm
  - utter_happy

<!-- ## sad path 2
* cumprimentar
  - utter_cumprimentar
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_despedir

## dando tchau
* despedir
  - utter_despedir -->

<!-- ## Informacoes do prefeito
* nome_prefeito{"cidade":"São Paulo"}
  - action_get_prefeito 
  - utter_nomeprefeito
 -->

<!-- ## interactive_story_1
* cumprimentar
    - utter_cumprimentar
* informar_nome{"nome": "Euristenho"}
    - slot{"nome": "Euristenho"}
    - utter_perguntar_ajuda
* nome_prefeito{"cidade": "Mossoró"}
    - slot{"cidade": "Mossoró"}
    - action_get_prefeito
    - utter_nomeprefeito
* affirm
    - utter_happy
    - utter_despedir -->

