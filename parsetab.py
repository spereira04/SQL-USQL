
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'A ACTUALIZA ADD_COLUMN AGREGA AGRUPANDO ALL ALTER_TABLE BETWEEN BORRA BY CAMBIA CAST CLAVE COLUMNA COMO CONTANDO COUNT CREA CREATE_TABLE DE DEFAULT DEFECTO DEL DELETE_FROM DISTINCT DISTINTOS DONDE DROP_COLUMN DROP_TABLE ELIMINA EN ENTRE ES ESTO EXISTE EXISTS FILLER FOREIGN_KEY FROM GROUP GROUP_BY HAVING IN INSERT_INTO IS_NULL JOIN LA LIKE LIMIT LOS METE MEZCLANDO MUCHO NO NOT_NULL NULO ON ORDENA ORDER_BY PARECIDO POR PRIMA PRIMARY_KEY REFERENTE SELECT SET SETEA TABLA TIRA TODO TRAEME TRANSFORMA UNICO UNIQUE UPDATE VALORES VALUES WHEREexpression : x\n                  | yx : x xy : AGRUPANDO POR\n            | LOS DISTINTOS\n            | METE EN\n            | LOS VALORES\n            | ORDENA POR\n            | COMO MUCHO\n            | EN ESTO\n            | PARECIDO A\n            | ES NULO\n            | POR DEFECTO\n            | CLAVE PRIMA\n            | CLAVE REFERENTE\n            | NO NULO\n            | TRANSFORMA Ay : DE LA TABLA\n            | BORRA DE LA\n            | CAMBIA LA TABLA\n            | AGREGA LA COLUMNA\n            | ELIMINA LA COLUMNA\n            | CREA LA TABLA\n            | TIRA LA TABLAy : WHERE DEL GROUP BYy : y yx : SELECT\n         | FROM\n         | WHERE\n         | ALL\n         | GROUP_BY\n         | JOIN\n         | ON\n         | DISTINCT\n         | COUNT\n         | INSERT_INTO\n         | VALUES\n         | UPDATE\n         | SET\n         | DELETE_FROM\n         | ORDER_BY\n         | LIMIT\n         | HAVING\n         | EXISTS\n         | IN\n         | BETWEEN\n         | LIKE\n         | IS_NULL\n         | ALTER_TABLE\n         | ADD_COLUMN\n         | DROP_COLUMN\n         | CREATE_TABLE\n         | DROP_TABLE\n         | DEFAULT\n         | UNIQUE\n         | PRIMARY_KEY\n         | FOREIGN_KEY\n         | NOT_NULL\n         | CAST\n         | FILLERy : TRAEME\n        | DONDE\n        | MEZCLANDO\n        | EN\n        | CONTANDO\n        | ACTUALIZA\n        | SETEA\n        | EXISTE\n        | ENTRE\n        | UNICO\n        | TODO\n        | FILLER'
    
_lr_action_items = {'SELECT':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[4,4,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,4,-29,-60,]),'FROM':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[5,5,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,5,-29,-60,]),'WHERE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,42,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[6,68,71,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,68,-29,-60,71,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'ALL':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[7,7,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,7,-29,-60,]),'GROUP_BY':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[8,8,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,8,-29,-60,]),'JOIN':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[9,9,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,9,-29,-60,]),'ON':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[10,10,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,10,-29,-60,]),'DISTINCT':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[11,11,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,11,-29,-60,]),'COUNT':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[12,12,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,12,-29,-60,]),'INSERT_INTO':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[13,13,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,13,-29,-60,]),'VALUES':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[14,14,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,14,-29,-60,]),'UPDATE':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[15,15,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,15,-29,-60,]),'SET':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[16,16,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,16,-29,-60,]),'DELETE_FROM':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[17,17,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,17,-29,-60,]),'ORDER_BY':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[18,18,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,18,-29,-60,]),'LIMIT':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[19,19,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,19,-29,-60,]),'HAVING':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[20,20,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,20,-29,-60,]),'EXISTS':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[21,21,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,21,-29,-60,]),'IN':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[22,22,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,22,-29,-60,]),'BETWEEN':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[23,23,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,23,-29,-60,]),'LIKE':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[24,24,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,24,-29,-60,]),'IS_NULL':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[25,25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,25,-29,-60,]),'ALTER_TABLE':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[26,26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,26,-29,-60,]),'ADD_COLUMN':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[27,27,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,27,-29,-60,]),'DROP_COLUMN':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[28,28,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,28,-29,-60,]),'CREATE_TABLE':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[29,29,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,29,-29,-60,]),'DROP_TABLE':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[30,30,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,30,-29,-60,]),'DEFAULT':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[31,31,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,31,-29,-60,]),'UNIQUE':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[32,32,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,32,-29,-60,]),'PRIMARY_KEY':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[33,33,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,33,-29,-60,]),'FOREIGN_KEY':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[34,34,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,34,-29,-60,]),'NOT_NULL':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[35,35,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,35,-29,-60,]),'CAST':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,67,68,69,],[36,36,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,36,-29,-60,]),'FILLER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,42,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[37,69,72,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,69,-29,-60,72,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'AGRUPANDO':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[38,38,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,38,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'LOS':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[40,40,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,40,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'METE':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[41,41,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,41,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'ORDENA':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[43,43,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,43,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'COMO':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[44,44,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,44,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'EN':([0,3,37,41,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[42,42,-72,78,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,42,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'PARECIDO':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[45,45,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,45,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'ES':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[46,46,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,46,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'POR':([0,3,37,38,42,43,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[39,39,-72,74,-64,80,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,39,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'CLAVE':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[47,47,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,47,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'NO':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[48,48,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,48,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'TRANSFORMA':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[49,49,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,49,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'DE':([0,3,37,42,51,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[50,50,-72,-64,89,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,50,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'BORRA':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[51,51,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,51,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'CAMBIA':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[52,52,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,52,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'AGREGA':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[53,53,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,53,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'ELIMINA':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[54,54,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,54,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'CREA':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[55,55,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,55,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'TIRA':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[56,56,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,56,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'TRAEME':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[57,57,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,57,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'DONDE':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[58,58,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,58,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'MEZCLANDO':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[59,59,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,59,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'CONTANDO':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[60,60,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,60,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'ACTUALIZA':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[61,61,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,61,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'SETEA':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[62,62,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,62,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'EXISTE':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[63,63,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,63,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'ENTRE':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[64,64,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,64,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'UNICO':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[65,65,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,65,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'TODO':([0,3,37,42,57,58,59,60,61,62,63,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[66,66,-72,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,66,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,42,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,],[0,-1,-2,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-64,-61,-62,-63,-65,-66,-67,-68,-69,-70,-71,-3,-29,-60,-26,-72,-4,-13,-5,-7,-6,-10,-8,-9,-11,-12,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,]),'DEL':([6,71,],[73,73,]),'DEFECTO':([39,],[75,]),'DISTINTOS':([40,],[76,]),'VALORES':([40,],[77,]),'ESTO':([42,],[79,]),'MUCHO':([44,],[81,]),'A':([45,49,],[82,87,]),'NULO':([46,48,],[83,86,]),'PRIMA':([47,],[84,]),'REFERENTE':([47,],[85,]),'LA':([50,52,53,54,55,56,89,],[88,90,91,92,93,94,97,]),'GROUP':([73,],[95,]),'TABLA':([88,90,93,94,],[96,98,101,102,]),'COLUMNA':([91,92,],[99,100,]),'BY':([95,],[103,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,],[1,]),'x':([0,2,67,],[2,67,67,]),'y':([0,3,70,],[3,70,70,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> x','expression',1,'p_std','parser_service.py',31),
  ('expression -> y','expression',1,'p_std','parser_service.py',32),
  ('x -> x x','x',2,'p_expression_english','parser_service.py',36),
  ('y -> AGRUPANDO POR','y',2,'p_assemble_subtokens_of_two','parser_service.py',40),
  ('y -> LOS DISTINTOS','y',2,'p_assemble_subtokens_of_two','parser_service.py',41),
  ('y -> METE EN','y',2,'p_assemble_subtokens_of_two','parser_service.py',42),
  ('y -> LOS VALORES','y',2,'p_assemble_subtokens_of_two','parser_service.py',43),
  ('y -> ORDENA POR','y',2,'p_assemble_subtokens_of_two','parser_service.py',44),
  ('y -> COMO MUCHO','y',2,'p_assemble_subtokens_of_two','parser_service.py',45),
  ('y -> EN ESTO','y',2,'p_assemble_subtokens_of_two','parser_service.py',46),
  ('y -> PARECIDO A','y',2,'p_assemble_subtokens_of_two','parser_service.py',47),
  ('y -> ES NULO','y',2,'p_assemble_subtokens_of_two','parser_service.py',48),
  ('y -> POR DEFECTO','y',2,'p_assemble_subtokens_of_two','parser_service.py',49),
  ('y -> CLAVE PRIMA','y',2,'p_assemble_subtokens_of_two','parser_service.py',50),
  ('y -> CLAVE REFERENTE','y',2,'p_assemble_subtokens_of_two','parser_service.py',51),
  ('y -> NO NULO','y',2,'p_assemble_subtokens_of_two','parser_service.py',52),
  ('y -> TRANSFORMA A','y',2,'p_assemble_subtokens_of_two','parser_service.py',53),
  ('y -> DE LA TABLA','y',3,'p_assemble_subtokens_of_tree','parser_service.py',57),
  ('y -> BORRA DE LA','y',3,'p_assemble_subtokens_of_tree','parser_service.py',58),
  ('y -> CAMBIA LA TABLA','y',3,'p_assemble_subtokens_of_tree','parser_service.py',59),
  ('y -> AGREGA LA COLUMNA','y',3,'p_assemble_subtokens_of_tree','parser_service.py',60),
  ('y -> ELIMINA LA COLUMNA','y',3,'p_assemble_subtokens_of_tree','parser_service.py',61),
  ('y -> CREA LA TABLA','y',3,'p_assemble_subtokens_of_tree','parser_service.py',62),
  ('y -> TIRA LA TABLA','y',3,'p_assemble_subtokens_of_tree','parser_service.py',63),
  ('y -> WHERE DEL GROUP BY','y',4,'p_assemble_subtokens_of_four','parser_service.py',67),
  ('y -> y y','y',2,'p_expression_spanish','parser_service.py',72),
  ('x -> SELECT','x',1,'p_spanish_translate','parser_service.py',76),
  ('x -> FROM','x',1,'p_spanish_translate','parser_service.py',77),
  ('x -> WHERE','x',1,'p_spanish_translate','parser_service.py',78),
  ('x -> ALL','x',1,'p_spanish_translate','parser_service.py',79),
  ('x -> GROUP_BY','x',1,'p_spanish_translate','parser_service.py',80),
  ('x -> JOIN','x',1,'p_spanish_translate','parser_service.py',81),
  ('x -> ON','x',1,'p_spanish_translate','parser_service.py',82),
  ('x -> DISTINCT','x',1,'p_spanish_translate','parser_service.py',83),
  ('x -> COUNT','x',1,'p_spanish_translate','parser_service.py',84),
  ('x -> INSERT_INTO','x',1,'p_spanish_translate','parser_service.py',85),
  ('x -> VALUES','x',1,'p_spanish_translate','parser_service.py',86),
  ('x -> UPDATE','x',1,'p_spanish_translate','parser_service.py',87),
  ('x -> SET','x',1,'p_spanish_translate','parser_service.py',88),
  ('x -> DELETE_FROM','x',1,'p_spanish_translate','parser_service.py',89),
  ('x -> ORDER_BY','x',1,'p_spanish_translate','parser_service.py',90),
  ('x -> LIMIT','x',1,'p_spanish_translate','parser_service.py',91),
  ('x -> HAVING','x',1,'p_spanish_translate','parser_service.py',92),
  ('x -> EXISTS','x',1,'p_spanish_translate','parser_service.py',93),
  ('x -> IN','x',1,'p_spanish_translate','parser_service.py',94),
  ('x -> BETWEEN','x',1,'p_spanish_translate','parser_service.py',95),
  ('x -> LIKE','x',1,'p_spanish_translate','parser_service.py',96),
  ('x -> IS_NULL','x',1,'p_spanish_translate','parser_service.py',97),
  ('x -> ALTER_TABLE','x',1,'p_spanish_translate','parser_service.py',98),
  ('x -> ADD_COLUMN','x',1,'p_spanish_translate','parser_service.py',99),
  ('x -> DROP_COLUMN','x',1,'p_spanish_translate','parser_service.py',100),
  ('x -> CREATE_TABLE','x',1,'p_spanish_translate','parser_service.py',101),
  ('x -> DROP_TABLE','x',1,'p_spanish_translate','parser_service.py',102),
  ('x -> DEFAULT','x',1,'p_spanish_translate','parser_service.py',103),
  ('x -> UNIQUE','x',1,'p_spanish_translate','parser_service.py',104),
  ('x -> PRIMARY_KEY','x',1,'p_spanish_translate','parser_service.py',105),
  ('x -> FOREIGN_KEY','x',1,'p_spanish_translate','parser_service.py',106),
  ('x -> NOT_NULL','x',1,'p_spanish_translate','parser_service.py',107),
  ('x -> CAST','x',1,'p_spanish_translate','parser_service.py',108),
  ('x -> FILLER','x',1,'p_spanish_translate','parser_service.py',109),
  ('y -> TRAEME','y',1,'p_english_translate','parser_service.py',113),
  ('y -> DONDE','y',1,'p_english_translate','parser_service.py',114),
  ('y -> MEZCLANDO','y',1,'p_english_translate','parser_service.py',115),
  ('y -> EN','y',1,'p_english_translate','parser_service.py',116),
  ('y -> CONTANDO','y',1,'p_english_translate','parser_service.py',117),
  ('y -> ACTUALIZA','y',1,'p_english_translate','parser_service.py',118),
  ('y -> SETEA','y',1,'p_english_translate','parser_service.py',119),
  ('y -> EXISTE','y',1,'p_english_translate','parser_service.py',120),
  ('y -> ENTRE','y',1,'p_english_translate','parser_service.py',121),
  ('y -> UNICO','y',1,'p_english_translate','parser_service.py',122),
  ('y -> TODO','y',1,'p_english_translate','parser_service.py',123),
  ('y -> FILLER','y',1,'p_english_translate','parser_service.py',124),
]
