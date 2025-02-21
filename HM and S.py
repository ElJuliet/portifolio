

def hor_s(horario:str):
 horario
 horario_hs=horario[0:2]
 hor_ts= int(horario_hs) * 3600
 #print(hor_ts)

 horario_ms=horario[3:5]
 min_ts= int(horario_ms) * 60
 #print(min_ts)

 horario_ss=horario[6:8]
 seg_ts= int(horario_ss) 
 #print(seg_ts)

 hor_tt= hor_ts + min_ts + seg_ts

 return hor_tt

print(hor_s("00:00:03"))
 
