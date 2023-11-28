import geopandas as gp
import pandas as pd
import pyogrio, os
from shapely.geometry import Point
from subprocess import run

def get_global_data(df: pd.DataFrame, csv_path: str) -> dict:
    global_data_df = pd.read_csv(csv_path, header=None, delimiter=":;", nrows=7, decimal=",", engine="python", encoding="ansi").transpose()

    global_data_dict_temp = global_data_df.to_dict('split', index=False)

    global_data_dict = dict()
    for idx, value in enumerate(global_data_dict_temp["data"][0]):
        global_data_dict[value] = global_data_dict_temp["data"][1][idx]

    global_data_dict["geometry"] = Point([global_data_dict["LONGITUDE"], global_data_dict["LATITUDE"]])

    return global_data_dict

def add_in_dataFrame(df1: pd.DataFrame, csv_path: str) -> pd.DataFrame:
    global_data = get_global_data(df1, csv_path)

    df2 = pd.read_csv(csv_path, delimiter=";", skiprows=8, decimal=",", encoding="ansi").drop(columns=["Unnamed: 19"])

    df2 = df2.assign(**global_data)

    return pd.concat([df1,df2], ignore_index=True)

def save_dataFrame(df: pd.DataFrame, shp_path: str) -> None:
    geo_df = gp.GeoDataFrame(df, geometry="geometry", crs="EPSG:4326")

    geo_df.fillna(0, inplace=True)

    geo_df = geo_df.convert_dtypes()

    geo_df.columns = ["data", "horario", "precip_T", "presATM", "presATMmax", "presATMmin", "radiacao", "temp_ar_BS",
                     "temp_orv", "tempMAX", "tempORVmax", "tempORVmin", "umidadeMAX", "umidadeMIN", "umidade", "ventoDIR",
                     "ventVELmax", "vel_vento", "regiao", "uf", "estacao", "codigo", "lat", "long", "alt", "data_fund", "geometry"]
    
    geo_df.to_file(shp_path, driver="ESRI Shapefile", encoding="utf-8", engine="pyogrio")

if __name__ == "__main__":
    path_to_files = "files_to_convert/"
    
    df = pd.DataFrame()

    for filepath in os.listdir(path_to_files):
        if filepath == ".gitkeep": continue
        df = add_in_dataFrame(df, path_to_files+filepath)

    save_dataFrame(df, "shapefiles/estacao.shp")