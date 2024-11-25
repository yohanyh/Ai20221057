import tkinter as tk
from tkinter import messagebox
from sklearn.ensemble import IsolationForest
import numpy as np

def detect_anomalies():
    try:
        # 사용자가 입력한 데이터를 가져오기
        data = entry.get("1.0", "end").strip()
        if not data:
            messagebox.showerror("입력 오류", "거래 금액 데이터를 입력해주세요!")
            return

        # 데이터 처리
        amounts = list(map(float, data.split(",")))

        # IsolationForest를 사용한 이상 감지
        model = IsolationForest(contamination=0.1, random_state=42)
        reshaped_data = np.array(amounts).reshape(-1, 1)
        predictions = model.fit_predict(reshaped_data)
        results = ["이상 거래" if p == -1 else "정상 거래" for p in predictions]

        # 결과 창 출력
        result_text = "거래 금액 및 이상 거래 결과:\n\n"
        for amount, result in zip(amounts, results):
            result_text += f"거래 금액: {amount:.2f} -> {result}\n"

        result_label.config(text=result_text)
    except Exception as e:
        messagebox.showerror("오류", f"처리 중 오류 발생: {e}")

# Tkinter GUI 설정
root = tk.Tk()
root.title("금융 거래 이상 감지 프로그램")
root.geometry("500x400")

# 제목
title_label = tk.Label(root, text="금융 거래 이상 감지 시스템", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# 설명
description_label = tk.Label(root, text="거래 금액을 쉼표(,)로 구분하여 입력하세요.\n예시: 200,15000,350,10000,250", font=("Arial", 10))
description_label.pack(pady=5)

# 데이터 입력 필드
entry = tk.Text(root, height=5, width=50, font=("Arial", 12))
entry.pack(pady=10)

# 분석 버튼
analyze_button = tk.Button(root, text="이상 거래 분석", command=detect_anomalies, bg="#4CAF50", fg="white", padx=10, pady=5)
analyze_button.pack(pady=10)

# 결과 표시 라벨
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# 프로그램 실행
root.mainloop()
