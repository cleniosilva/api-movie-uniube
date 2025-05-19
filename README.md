
## Aplicação de filmes


### Configurando ambiente

 * Criando venv python

````commandline
python3.12 -m venv .venv
````

 * Ativando virtualenv no windows

```
.venv\Scripts\activate.ps1
.venv\Scripts\activate.bat
```
 * Ativando virtualenv no linux

````commandline
source .venv/activate/bin
````

### Instalando fastapi

````commandline
pip install fastapi uvicorn 
````

### Executar a aplicação


````commandline
uvicorn presentation.fastapi.main:app --reload
````
