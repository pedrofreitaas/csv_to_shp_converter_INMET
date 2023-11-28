## Converter to SHP using .csv files (INMET .csv's only).

# Usage:

```python
'''
1º) Put the .csv files inside the "files_to_convert/" folder.
2º) Run the script.
3º) The result shapefiles should be inside the "shapefiles/folder", all collapsed in one single shapefile.
'''
```

# OBS: .csv files have to come the the source INMET.

# Column name explanations:
```python
{
    "data":"Data da medicao.",
    "horario":"Horario da medicao",
    "precip_T":"Precipitacao total no horario da medicao (mm).",
    "presATM":"Pressao Atmosférica ao nivel da estacao no horario (mB).",
    "presATMmax":"Pressão Atmosterica maxima na hora anterior (mB).",    
    "presATMmin":"Pressão Atmosterica minima na hora anterior (mB).",    
    "radiacao":"Radiacao global. (Kj/m�)",
    "temp_ar_BS":"Temperatura do Ar (Bulbo Seco), horaria, celsius.",    
    "temp_orv":"Temperatura do ponto de orvalho, em celsius.",
    "tempMAX":"Temperatura maxima, hora anterior.",
    "tempORVmax":"Temperatura minima, hora anterior.",
    "tempORVmin":"Temperatura ORVALHO maxima, hora anterior.",
    "umidadeMAX":"Temperatura ORVALHO minima, hora anterior.",
    "umidadeMIN":"Umidade relativa maxima, hora anterior.",
    "umidade":"Umidade relativa minima, hora anterior.",
    "ventoDIR":"Umidade relativa do ar, no horario.",
    "ventVELmax":"Direção do vento, no horario.",
    "vel_vento":"Rajada máxima de vento.",
    "regiao":"Velocidade vento",
    "uf":"Regiao brasileira em que o medidor foi instalado.",
    "estacao":"Unidade federativa brasileira de instalacao do medidor.",
    "codigo":"Nome do medidor",
    "lat":"Codigo do medidor",
    "long":"Latitude geografica de instalacao do medidor.",
    "alt":"Longetude geografica de instalacao do medidor.",
    "data_fund":"Altitude em que o medidor foi instalado",
    "geometry":"Data de instalacao do medidor"
}
```