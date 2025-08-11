estudiantes = 85
capacidad_autobus = 12
estudiantes_en_autobuses_completos = (estudiantes // capacidad_autobus) * capacidad_autobus
estudiantes_sin_lugar = estudiantes % capacidad_autobus


print(f"{estudiantes_sin_lugar} estudiantes no alcanzan lugar en los autobuses completos.")
