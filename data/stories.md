## caminho feliz
* cumprimentar
  - utter_cumprimentar
  - slot{"nome":"jorge alberto"}
* informar_nome{"nome": "jorge alberto"}
  - utter_perguntar_ajuda 
  - slot{"cidade":"São Paulo"}  
* nome_prefeito{"cidade":"São Paulo"}
  - action_get_prefeito 
  - utter_nomeprefeito
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
  - utter_nomeprefeito

