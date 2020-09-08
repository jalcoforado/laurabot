## caminho feliz
* cumprimentar
  - utter_cumprimentar
* informar_nome{"nome": "jorge"}
  - slot{"nome": "jorge"}
  - utter_perguntar_ajuda
* nome_prefeito{"cidade":"São Paulo"}
  - slot{"cidade": "São Paulo"}
  - action_get_prefeito 
  - slot{"cidade": "none"} 
  - utter_nomeprefeito
* affirm
  - utter_happy
  - utter_despedir

## sad path 1
* cumprimentar
  - utter_cumprimentar
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* cumprimentar
  - utter_cumprimentar
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_despedir

## dando tchau
* despedir
  - utter_despedir

## Informacoes do prefeito
* nome_prefeito{"cidade":"São Paulo"}
  - action_get_prefeito 
  - slot{"cidade": "none"} 
  - utter_nomeprefeito

