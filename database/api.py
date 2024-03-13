from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import sqlite3
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

class Input(BaseModel):
    nome: str
    email: str

@app.post("/teste2")
def teste2(inputs: Input) -> str:
    try:
        with sqlite3.connect('teste.db') as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO usuarios (nome,email) VALUES (?,?)", (inputs.nome, inputs.email))
            conn.commit()
            return f"Inserção bem sucedida: Nome: {inputs.nome}, Email: {inputs.email}"
    except Exception as e:
        return f"Erro ao inserir no banco de dados: {str(e)}"

@app.get("/usuarios")
def listar_usuarios():
    try:
        with sqlite3.connect('teste.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM usuarios")
            usuarios = cur.fetchall()
            return {"usuarios": usuarios}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar usuários: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
