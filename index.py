"""
serve.py

저장된 model.pkl을 로드해 FastAPI 서버로 예측 API를 제공
"""
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# (1) FastAPI 앱 생성
app = FastAPI()

# (2) 모델 로드
model = joblib.load("model.pkl")
print("Model loaded successfully.")

# (3) 예측 요청 바디 정의(pydantic)
class PredictRequest(BaseModel):
    data: list

"""
data는 예:
[
  [1.2],
  [3.4],
  ...
]
즉 2차원 리스트 형태로 가정
"""

# (4) 예측 엔드포인트
@app.post("/predict")
def predict(request: PredictRequest):
    # list -> numpy array 변환
    X_input = np.array(request.data)
    preds = model.predict(X_input)

    # numpy array를 파이썬 기본 타입으로 변환하여 반환
    return {"predictions": preds.flatten().tolist()}
