from fastapi import FastAPI, HTTPException
import yaml
from pathlib import Path
import asyncio

app = FastAPI()
lock = asyncio.Lock()  # Para manejar la concurrencia

# Leer el archivo YAML al iniciar
dui_path = Path(__file__).resolve().parents[2] / "data" / "duis.yaml"
with open(dui_path, "r", encoding="utf-8") as file:
    data = yaml.safe_load(file).get("default", {})

# Lista de DUIs y un set para los entregados
available_duis = data.get("duis")
assigned_duis = set()


@app.get("/dui")
async def get_unique_dui():
    async with lock:
        for dui in available_duis:
            num = dui["numero"]
            if num not in assigned_duis:
                assigned_duis.add(num)
                return {"dui": dui}

        # Si no hay más DUIs disponibles
        raise HTTPException(status_code=404, detail="No hay más DUIs disponibles")
