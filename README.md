# URL Shortener – FastAPI + SQLite

Una piccola API REST di esempio per un servizio di URL shortening.

---
## Installazione
```bash
# 1 – crea e attiva un virtualenv
$ python -m venv .venv
$ source .venv/bin/activate

# 2 – installa i requirements
$ pip install -r requirements.txt
```

---

## Avviare l’API
Dalla root del  progetto
```bash
$ python fastapi dev ./src/url_shortener/asgi.py --reload
```

---

## Database & Migrazioni (Alembic)

Il database di default è un file SQLite chiamato `shortener.db` nella root di `src/url_shortener` (configurato in `database.py`).

### 1 – Inizializzare Alembic (solo prima volta e già fatto per questo progetto)

```bash
$ alembic init alembic          # crea la cartella alembic/ e alembic.ini
```

Il repo d’esempio ha già questi file. Se non li hai, esegui il comando sopra.

### 2 – Configurare *alembic/env.py* (già fatto per questo progetto)

  ```python
  import url_shortener.models  # noqa: F401 (side‑effects)
  target_metadata = Base.metadata
  ```

### 3 – Creare una migration
Modifica il messaggio con il nome della migrazione.

```bash
# Autogenera tenendo conto dei modelli ORM
$ alembic revision --autogenerate -m "create urls table"
```

### 4 – Applicare le migration

```bash
$ alembic upgrade head
```

Dopo l’upgrade troverai `shortener.db` con la tabella `urls`.

> Usa la stessa procedura ogni volta che modifichi i modelli.

---

## Comandi rapidi

| Azione             | Comando                                                   |
| ------------------ | --------------------------------------------------------- |
| Avviare API (dev)  | `python fastapi dev ./src/url_shortener/asgi.py --reload` |
| Crea migrazione    | `alembic revision --autogenerate -m "…"`                  |
| Applica migrazione | `alembic upgrade head`                                    |

---

## Struttura progetto

```
url_shortener/           ⟵ root del progetto
├─ .venv/                ⟵ virtualenv (non committare)
├─ alembic/              ⟵ migrazioni e env.py
├─ src/
│  └─ url_shortener/
│     ├─ __init__.py
│     ├─ asgi.py         ⟵ istanza FastAPI `app`
│     ├─ database.py     ⟵ engine, SessionLocal, Base, get_db()
│     ├─ models.py       ⟵ ORM models (Url, …)
│     └─ views.py        ⟵ router example
├─ alembic.ini
├─ requirements.txt
└─ README.md
```
## Documentazione
[FastAPI](https://fastapi.tiangolo.com/)
[SQLAlchemy ](https://www.sqlalchemy.org/)

---

Buon divertimento!
****
