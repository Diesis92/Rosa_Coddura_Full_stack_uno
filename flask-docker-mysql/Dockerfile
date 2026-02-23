# Usa immagine ufficiale Python
FROM python:3.11

# Crea la cartella /app e rendila cartella di lavoro
WORKDIR /app

# Copia solo requirements.txt prima (per sfruttare cache)
COPY requirements.txt .

# Installa le librerie Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il resto del progetto dentro /app
COPY . .

# Comando di avvio del container
CMD ["python", "app.py"]