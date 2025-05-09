import pandas as pd

def filtra_annotazioni(df, Sistema):
    if Sistema == 'M':
        return df[df['SISTEMA'] == 'MEDCAT'].copy()
    
    elif Sistema == 'B':
        return df[df['SISTEMA'] == 'BIOPORTAL'].copy()
    
    elif Sistema == 'B_AND_M':
        # Trova le triple (A, VOC, C) comuni ai due sistemi
        medcat_triples = set(df[df['SISTEMA'] == 'MEDCAT'][['A', 'VOC', 'C']].apply(tuple, axis=1))
        bioportal_triples = set(df[df['SISTEMA'] == 'BIOPORTAL'][['A', 'VOC', 'C']].apply(tuple, axis=1))
        comuni = medcat_triples & bioportal_triples

        # Seleziona le righe relative alle triple comuni
        df_comuni = df[df.apply(lambda row: (row['A'], row['VOC'], row['C']) in comuni, axis=1)].copy()

        # Imposta il campo SISTEMA come MEDCAT_AND_BIOPORTAL
        df_comuni['SISTEMA'] = 'MEDCAT_AND_BIOPORTAL'
        return df_comuni

    else:
        raise ValueError("Parametro Sistema non valido. Usa 'M', 'B' o 'B_AND_M'.")
        
        
        
data = [
    {'A': 'fever', 'VOC': 'SNOMED', 'C': '12345', 'i': 1, 'SISTEMA': 'MEDCAT'},
    {'A': 'fever', 'VOC': 'SNOMED', 'C': '12346', 'i': 2, 'SISTEMA': 'MEDCAT'},
    {'A': 'fever', 'VOC': 'SNOMED', 'C': '10000', 'i': 3, 'SISTEMA': 'MEDCAT'},
    {'A': 'cough', 'VOC': 'SNOMED', 'C': '54321', 'i': 1, 'SISTEMA': 'MEDCAT'},
    {'A': 'fever', 'VOC': 'SNOMED', 'C': '12345', 'i': 1, 'SISTEMA': 'BIOPORTAL'},
    {'A': 'fever', 'VOC': 'SNOMED', 'C': '10000', 'i': 2, 'SISTEMA': 'BIOPORTAL'},
    {'A': 'cough', 'VOC': 'SNOMED', 'C': '54321', 'i': 1, 'SISTEMA': 'BIOPORTAL'},
    {'A': 'pain',  'VOC': 'SNOMED', 'C': '11111', 'i': 1, 'SISTEMA': 'BIOPORTAL'}
]

df = pd.DataFrame(data)

result = filtra_annotazioni(df, 'B_AND_M')
print(result)



def filtra_annotazioni(df, Sistema):
    if Sistema == 'M':
        return df[df['SISTEMA'] == 'MEDCAT'].copy()

    elif Sistema == 'B':
        return df[df['SISTEMA'] == 'BIOPORTAL'].copy()

    elif Sistema == 'B_AND_M':
        medcat_triples = set(df[df['SISTEMA'] == 'MEDCAT'][['A', 'VOC', 'C']].apply(tuple, axis=1))
        bioportal_triples = set(df[df['SISTEMA'] == 'BIOPORTAL'][['A', 'VOC', 'C']].apply(tuple, axis=1))
        comuni = medcat_triples & bioportal_triples

        df_comuni = df[df.apply(lambda row: (row['A'], row['VOC'], row['C']) in comuni, axis=1)].copy()
        df_comuni['SISTEMA'] = 'MEDCAT_AND_BIOPORTAL'
        return df_comuni

    elif Sistema == 'B_OR_M':
        medcat_df = df[df['SISTEMA'] == 'MEDCAT']
        bioportal_df = df[df['SISTEMA'] == 'BIOPORTAL']

        all_triples = pd.concat([medcat_df, bioportal_df])[['A', 'VOC', 'C']].drop_duplicates()

        # Trova triple che non sono comuni
        already_present = df[['A', 'VOC', 'C', 'SISTEMA']]
        existing_combos = set(already_present.apply(tuple, axis=1))

        rows = []
        for _, row in all_triples.iterrows():
            a, voc, c = row['A'], row['VOC'], row['C']
            matching_rows = df[(df['A'] == a) & (df['VOC'] == voc) & (df['C'] == c)]
            for i_val in matching_rows['i'].unique():
                if ((a, voc, c, 'BIOPORTAL_OR_MEDCAT') not in existing_combos):
                    rows.append({'A': a, 'VOC': voc, 'C': c, 'i': i_val, 'SISTEMA': 'BIOPORTAL_OR_MEDCAT'})

        df_or = pd.DataFrame(rows)
        return df_or

    else:
        raise ValueError("Parametro Sistema non valido. Usa 'M', 'B', 'B_AND_M' o 'B_OR_M'.")
        
        
def filtra_annotazioni(df, Sistema):
    if Sistema == 'M':
        return df[df['SISTEMA'] == 'MEDCAT'].copy()

    elif Sistema == 'B':
        return df[df['SISTEMA'] == 'BIOPORTAL'].copy()

    elif Sistema == 'B_AND_M':
        medcat_triples = set(df[df['SISTEMA'] == 'MEDCAT'][['A', 'VOC', 'C']].apply(tuple, axis=1))
        bioportal_triples = set(df[df['SISTEMA'] == 'BIOPORTAL'][['A', 'VOC', 'C']].apply(tuple, axis=1))
        comuni = medcat_triples & bioportal_triples

        df_comuni = df[df.apply(lambda row: (row['A'], row['VOC'], row['C']) in comuni, axis=1)].copy()
        df_comuni['SISTEMA'] = 'MEDCAT_AND_BIOPORTAL'
        return df_comuni

    elif Sistema == 'B_OR_M':
        # Identifica triple comuni e triple uniche
        medcat = df[df['SISTEMA'] == 'MEDCAT']
        bioportal = df[df['SISTEMA'] == 'BIOPORTAL']

        medcat_triples = set(medcat[['A', 'VOC', 'C']].apply(tuple, axis=1))
        bioportal_triples = set(bioportal[['A', 'VOC', 'C']].apply(tuple, axis=1))
        comuni = medcat_triples & bioportal_triples

        # Righe con triple comuni -> rimosse da MEDCAT/BIOPORTAL, create nuove con BIOPORTAL_OR_MEDCAT
        comuni_df = df[df.apply(lambda row: (row['A'], row['VOC'], row['C']) in comuni and row['SISTEMA'] in ['MEDCAT', 'BIOPORTAL'], axis=1)]

        # Crea nuove righe con SISTEMA = BIOPORTAL_OR_MEDCAT
        nuovi = comuni_df.copy()
        nuovi['SISTEMA'] = 'BIOPORTAL_OR_MEDCAT'

        # Filtra via le righe originali di MEDCAT/BIOPORTAL con triple comuni
        df_filtrato = df[~df.apply(lambda row: (row['A'], row['VOC'], row['C']) in comuni and row['SISTEMA'] in ['MEDCAT', 'BIOPORTAL'], axis=1)]

        # Unisci con le nuove righe
        df_finale = pd.concat([df_filtrato, nuovi], ignore_index=True).sort_values(by=['A', 'i']).reset_index(drop=True)

        return df_finale

    else:
        raise ValueError("Parametro Sistema non valido. Usa 'M', 'B', 'B_AND_M' o 'B_OR_M'.")
        
data = [
    {'A': 'fever', 'VOC': 'SNOMED', 'C': '12345', 'i': 1, 'SISTEMA': 'MEDCAT'},
    {'A': 'fever', 'VOC': 'SNOMED', 'C': '12346', 'i': 2, 'SISTEMA': 'MEDCAT'},
    {'A': 'fever', 'VOC': 'SNOMED', 'C': '10000', 'i': 3, 'SISTEMA': 'MEDCAT'},
    {'A': 'cough', 'VOC': 'SNOMED', 'C': '54321', 'i': 1, 'SISTEMA': 'MEDCAT'},
    {'A': 'fever', 'VOC': 'SNOMED', 'C': '12345', 'i': 1, 'SISTEMA': 'BIOPORTAL'},
    {'A': 'fever', 'VOC': 'SNOMED', 'C': '10000', 'i': 2, 'SISTEMA': 'BIOPORTAL'},
    {'A': 'cough', 'VOC': 'SNOMED', 'C': '54321', 'i': 1, 'SISTEMA': 'BIOPORTAL'},
    {'A': 'pain',  'VOC': 'SNOMED', 'C': '11111', 'i': 1, 'SISTEMA': 'BIOPORTAL'}
]
df = pd.DataFrame(data)


         A     VOC      C  i              SISTEMA
0    fever  SNOMED  12346  2               MEDCAT
1     pain  SNOMED  11111  1            BIOPORTAL
2    fever  SNOMED  12345  1  BIOPORTAL_OR_MEDCAT
3    fever  SNOMED  10000  3  BIOPORTAL_OR_MEDCAT
4    fever  SNOMED  10000  2  BIOPORTAL_OR_MEDCAT
5    cough  SNOMED  54321  1  BIOPORTAL_OR_MEDCAT                        