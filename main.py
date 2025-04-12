from fastapi import FastAPI, HTTPException
from satcfdi import csf
import re

app = FastAPI()
app.title = "API Obtener información del cliente basado en CSF"
app.version = "1.1"

#Cuando contamos con el número de constancia y RFC se puede traer la información para validar algun cambio en el mismo
@app.get('/sat/csf/{rfc}/{id_cif}', tags=['SAT'])
def get_csf(rfc: str, id_cif: str):
   
    # Realizamos la consulta con el RFC y el ID de CIF
    try:
        res = csf.retrieve(rfc, id_cif=id_cif)
        if not res:
            raise HTTPException(status_code=404, detail="No se encontró información para el RFC y ID de CIF proporcionados.")
        return res
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error en los parámetros proporcionados: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}")


# Traer la información desde el código QR de la constacia de situación fiscal
@app.get('/sat/csf/qr/', tags=['SAT'])
def get_csf(url: str):
    # Intentamos extraer el valor de D3 de la URL
    match = re.search(r"D3=(\d+_\w+)", url)
    
    if not match:
        raise HTTPException(status_code=400, detail="La URL no corresponde a un QR de una Constancia de Situación Fiscal")
    
    D3 = match.group(1)
    idcif, rfc = D3.split('_')

    # Realizamos la consulta con el RFC y el ID de CIF
    try:
        res = csf.retrieve(rfc, id_cif=idcif)
        if not res:
            raise HTTPException(status_code=404, detail="No se encontró información para el RFC y ID de CIF proporcionados.")
        return res
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error en los parámetros proporcionados: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}")


