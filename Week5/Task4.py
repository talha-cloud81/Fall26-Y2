raw_temps = [22.5, "ERR", 18.0, None, 30.2, "ERR", 0.0]
result = [round(c*1.8+32,1) for c in raw_temps if isinstance(c,(int,float))]
print(result)