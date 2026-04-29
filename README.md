# Statistics-and-Data-Modeling-DES432

## Ecological Footprint and GDP Growth Analysis

โปรเจกต์นี้เป็นการวิเคราะห์ความสัมพันธ์ระหว่าง การเติบโตทางเศรษฐกิจ (GDP) และ ผลกระทบต่อสิ่งแวดล้อม (Ecological Footprint) ในหลายประเทศ โดยใช้เทคนิค

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Statistical Inference
- Regression Modeling


## 🛠 การติดตั้ง (Installation)

โปรเจกต์นี้พัฒนาด้วยภาษา Python จำเป็นต้องติดตั้ง Library ที่เกี่ยวข้องก่อนใช้งาน โดยรันคำสั่งต่อไปนี้ใน Terminal หรือ PowerShell:

```
python -m pip install pandas numpy matplotlib seaborn statsmodels scipy
```

## 📊 ข้อมูลที่ใช้ (Dataset)

ไฟล์ข้อมูล:
EF_GDP(constant2010USD).csv

Source: https://www.kaggle.com/datasets/thedevastator/national-ecological-footprint-and-gdp-growth-200?resource=download

ข้อมูลประกอบด้วย:

- Ecological Footprint (EF)
- Gross Domestic Product (GDP)
- การเปลี่ยนแปลงของข้อมูลระหว่างปี 2009 และ 2013

###  ตัวแปรที่ใช้ (Variables)

- EFDelta → การเปลี่ยนแปลงของ Ecological Footprint
- GDPDelta → การเติบโตของ GDP (ตัวแปรตาม Y)
- GDP2009 → ค่า GDP ตั้งต้น (ตัวแปรอิสระ X)

##  วัตถุประสงค์ (Objective)

เพื่อศึกษาว่าการเติบโตทางเศรษฐกิจสัมพันธ์กับการเพิ่มขึ้นของผลกระทบต่อสิ่งแวดล้อมหรือไม่

##  วิธีการใช้งาน (Usage)

เมื่อรันโปรแกรม project.py กราฟจะแสดงขึ้นมาตามลำดับดังนี้:

### 📈 หน้าต่างที่ 1: Distribution of GDP Growth

แสดง Histogram ของ GDPDelta เพื่อดูการกระจายตัวของการเติบโตทางเศรษฐกิจ

### 📊 หน้าต่างที่ 2: EFDelta vs GDPDelta

แสดง Scatterplot เพื่อดูความสัมพันธ์ระหว่าง: การเปลี่ยนแปลงของสิ่งแวดล้อม และ การเติบโตทางเศรษฐกิจ

### 📉 หน้าต่างที่ 3: Regression Analysis

แสดง Regression Line พร้อมค่า Correlation (r) และ p-value

### 📉 หน้าต่างที่ 4: Residual Plot

แสดงความคลาดเคลื่อนของโมเดล (Residuals)

## 🔍 ผลลัพธ์ที่แสดง:

Coefficients (β): แสดงผลกระทบของตัวแปรอิสระต่อ GDPDelta

p-values: ใช้ทดสอบนัยสำคัญทางสถิติของแต่ละตัวแปร

r: แสดงให้เห็นถึงความสัมพันธ์ระหว่าง EFDelta และ GDPDelta
