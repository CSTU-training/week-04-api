'''
Author: Telliex telliexyuzo@gmail.com
Date: 2026-05-21 18:07:01
LastEditors: Telliex telliexyuzo@gmail.com
LastEditTime: 2026-05-21 18:07:35
FilePath: /week-03-api/main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from fastapi import FastAPI

app = FastAPI(title="Book Tracker API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to Book Tracker API"}

@app.get("/health")
def health():
    return {"status": "ok"}