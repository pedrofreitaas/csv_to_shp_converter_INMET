## Converter to SHP using .csv files (INMET .csv's only).

# Usage:

```python
'''
1º) Put the .csv files inside the "files_to_convert/" folder.
2º) Run the script.
3º) The result shapefiles should be inside the "shapefiles/folder", all collapsed in one single shapefile.
'''
```

### OBS: .csv files have to come from the source: Banco dados meteorológicos INMET.

### Column name explanations:
```python
{
    "id": "ID incremental atribuído a linha da tabela",
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
    "tempMIN":"Temperatura minima, hora anterior.",
    "tempORVmax":"Temperatura ORVALHO maxima, hora anterior.",
    "tempORVmin":"Temperatura ORVALHO minima, hora anterior.",
    "umidadeMAX":"Umidade relativa maxima, hora anterior.",
    "umidadeMIN":"Umidade relativa minima, hora anterior.",
    "umidade":"Umidade relativa do ar, no horario.",
    "ventoDIR":"Direção do vento, no horario.",
    "ventVELmax":"Rajada máxima de vento.",
    "vel_vento":"Velocidade vento",
    "regiao":"Regiao brasileira em que o medidor foi instalado.",
    "uf":"Unidade federativa brasileira de instalacao do medidor.",
    "estacao":"Nome do medidor",
    "codigo":"Codigo do medidor",
    "lat":"Latitude geografica de instalacao do medidor.",
    "long":"Longetude geografica de instalacao do medidor.",
    "alt":"Altitude em que o medidor foi instalado",
    "geometry":"Data de instalacao do medidor"
}
```