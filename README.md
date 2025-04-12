# API Obtener Información del Cliente Basado en CSF

## Descripción

API construida con **FastAPI** para obtener información de la **Constancia de Situación Fiscal (CSF)** del SAT. Proporciona dos endpoints: uno para consultar información usando RFC y ID de CIF, y otro para obtenerla a partir de un código QR del SAT.

## Instalación

1. **Clona el repositorio**:

    ```bash
    git clone https://github.com/rcvalderrabano/sat-constancia-fiscal-api.git
    cd sat-constancia-fiscal-api
    ```

2. **Instala las dependencias** usando `make`:

    ```bash
    make install
    ```

3. **Activa el entorno virtual** (si no se activa automáticamente):

    ```bash
    source venv/bin/activate  # En Linux/macOS
    venv\Scripts\activate     # En Windows
    ```

4. **Ejecuta el servidor**:

    ```bash
    make run
    ```

    El servidor se iniciará en [http://localhost:8000](http://localhost:8000).

## Uso de la API

### 1. Obtener información con RFC y ID de CIF

- **Endpoint**: `GET /sat/csf/{rfc}/{id_cif}`

    Ejemplo de solicitud:

    ```bash
    GET /sat/csf/XAXX010101000/999999999
    ```

**Ejemplo de respuesta para persona moral**:

```json
{
  "Regimenes": [
    {
      "RegimenFiscal": {
        "code": "601",
        "description": "General de Ley Personas Morales"
      },
      "Fecha de alta": "2020-03-31"
    }
  ],
  "Denominación o Razón Social": "TECHNOPROBE SPA",
  "Régimen de capital": "SAS DE CV",
  "Fecha de constitución": "2020-03-31",
  "Fecha de Inicio de operaciones": "2020-03-31",
  "Situación del contribuyente": "ACTIVO",
  "Fecha del último cambio de situación": "2020-03-31",
  "Entidad Federativa": "QUERETARO",
  "Municipio o delegación": "QUERETARO",
  "Colonia": "CIMATARIO",
  "Tipo de vialidad": "CALLE",
  "Nombre de la vialidad": "LUIS M VEGA",
  "Número exterior": "111",
  "Número interior": "C",
  "CP": "76030",
  "Correo electrónico": "rgacapitalfinance@outlook.com",
  "AL": "QUERETARO 1"
}

**Ejemplo de respuesta para persona fisica**:

```json
{
  "Regimenes": [
    {
      "RegimenFiscal": {
        "code": "605",
        "description": "Sueldos y Salarios e Ingresos Asimilados a Salarios"
      },
      "Fecha de alta": "2021-01-21"
    }
  ],
  "CURP": "CUVR870120HPLRLB00",
  "Nombre": "ROBERTO",
  "Apellido Paterno": "CRUZ",
  "Apellido Materno": "VALDERRABANO",
  "Fecha Nacimiento": "1987-01-20",
  "Fecha de Inicio de operaciones": "2009-02-18",
  "Situación del contribuyente": "REACTIVADO",
  "Fecha del último cambio de situación": "2021-01-21",
  "Entidad Federativa": "QUERETARO",
  "Municipio o delegación": "QUERETARO",
  "Colonia": "VIÑEDOS",
  "Tipo de vialidad": "CALLE",
  "Nombre de la vialidad": "CTO MERLOT",
  "Número exterior": "3023",
  "Número interior": "26",
  "CP": "76235",
  "Correo electrónico": "rcruz.valderrabano@gmail.com",
  "AL": "QUERETARO 1"
}


    ```

### 2. Obtener información usando un código QR

- **Endpoint**: `GET /sat/csf/qr/`

    Ejemplo de solicitud:

    ```bash
    GET /sat/csf/qr/?url=https://www.sat.gob.mx/constancia_fiscal?D3=XAXX010101000_99999999
    ```

    Ejemplo de respuesta (similar a la anterior).

## Licencia

Este proyecto está licenciado bajo la **Licencia GPL-3.0**. Puedes ver los términos completos en el archivo [LICENSE](LICENSE).
