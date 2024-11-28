# Use uma imagem base com Python
FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação para o contêiner
COPY . .

# Exponha a porta que a aplicação usará
EXPOSE 5000

# Defina o comando para iniciar a aplicação
CMD ["python", "app.py"]
