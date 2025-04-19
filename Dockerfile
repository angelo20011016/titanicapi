FROM python:3.11-slim

# 安裝 libgomp1 給 LightGBM 用
RUN apt-get update && apt-get install -y libgomp1

# 安裝相依套件
COPY requirements.txt .
RUN pip install -r requirements.txt

# 複製專案檔案進 container
COPY . .

# 執行 FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
