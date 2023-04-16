"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    filas=len(tbl0)
    return filas


def pregunta_02():
    cols=len(tbl0.columns)
    return cols


def pregunta_03():
    data_Sort=tbl0.sort_values('_c1')
    countval=data_Sort['_c1'].value_counts(sort=False)
    return countval


def pregunta_04():
    prom=tbl0.groupby(['_c1'])['_c2'].mean()
    return prom


def pregunta_05():
    max=tbl0.groupby(['_c1'])['_c2'].max()
    return max


def pregunta_06():
    lista1=[i.upper() for i in sorted(tbl1['_c4'].unique().tolist())]
    return lista1


def pregunta_07():
    suma=tbl0.groupby(['_c1'])['_c2'].sum()
    return suma


def pregunta_08():
    tbl0copy=tbl0.copy()
    tbl0copy['suma']=tbl0copy['_c0']+tbl0copy['_c2']
    return tbl0copy


def pregunta_09():
    tbl0_copy=tbl0.copy()
    tbl0_copy['year']=tbl0_copy['_c3'].apply(lambda x: x[:4])
    return tbl0_copy

def my_agg(x):
    names = {
	'_c2':','.join(list(x['_c2'].astype(str))).replace(',',':')
	}

    return pd.Series(names,index=['_c2'])

def pregunta_10():
    tbl02_copy=tbl0.copy()
    tbl02_copy=tbl02_copy.sort_values('_c2')
    tbl0_agg=tbl02_copy.groupby(["_c1"]).apply(my_agg)
    return tbl0_agg

def my_agg2(x):
    names = {
	'_c4':','.join(list(x['_c4'].astype(str)))
	}

    return pd.Series(names,index=['_c4'])

def pregunta_11():
    tbl12_copy=tbl1.copy()
    tbl12_copy=tbl12_copy.sort_values('_c4')
    tbl1_agg2=tbl12_copy.groupby(["_c0"]).apply(my_agg2).reset_index()
    return tbl1_agg2

def my_agg3(x):
    names = {
	'_c5': ','.join(x['_c5a'] + ':' + x['_c5b'].astype(str)),
    }

    return pd.Series(names,index=['_c5'])

def pregunta_12():
    tbl2_copy=tbl2.copy()
    tbl2_copy=tbl2_copy.sort_values('_c5a')
    tbl2_agg3=tbl2_copy.groupby(["_c0"]).apply(my_agg3).reset_index()
    return tbl2_agg3


def pregunta_13():
    tbl0_copy_m=tbl0.sort_values('_c0')
    tbl2_copy_m=tbl2.sort_values('_c0')
    tbl_merge=pd.merge(tbl2_copy_m,tbl0_copy_m, on="_c0")
    tbl_merge_agg=tbl_merge.groupby(['_c1'])['_c5b'].sum()
    return tbl_merge_agg
