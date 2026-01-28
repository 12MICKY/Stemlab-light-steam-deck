# Stemlab-light-stream-deck

โปรเจกต์สำหรับควบคุมอุปกรณ์ใน Home Assistant ผ่าน Stream Deck
ใช้ Python Script ในการสั่งงานแบบกดปุ่มเดียว เปิด/ปิด (Toggle)
ออกแบบมาให้ใช้งานจริง เสถียร และไม่เกิดปัญหา process ค้าง

---

## Features

* ควบคุมอุปกรณ์ด้วยปุ่มเดียว (Toggle ON/OFF)
* รองรับอุปกรณ์ประเภท light
* รองรับอุปกรณ์ประเภท switch
* รองรับอุปกรณ์ประเภท fan
* ใช้งานร่วมกับ Stream Deck ผ่าน Run Command
* สามารถทดสอบรันผ่าน Terminal ได้
* ไม่ใช้ while loop และไม่ต้องกด Ctrl+C
* ใช้งานผ่าน Python virtual environment

---

## Project Structure

```text
Stemlab-light-stream-deck/
├── venv/
├── .env
├── toggle_all.py
├── toggle_air_compressor.py
├── toggle_blower_fan.py
└── README.md
```

---

## Requirements

* Python 3.10 ขึ้นไป
* Home Assistant (เปิดใช้งาน REST API)
* Stream Deck
* Python libraries:

  * requests
  * python-dotenv

---

## Installation

### 1. สร้างโฟลเดอร์โปรเจกต์

```bash
mkdir Stemlab-light-stream-deck
cd Stemlab-light-stream-deck
```

### 2. สร้าง virtual environment

```bash
python3 -m venv venv
```

### 3. ติดตั้ง dependencies

```bash
venv/bin/pip install requests python-dotenv
```

---

## Environment Configuration

สร้างไฟล์ `.env` ภายในโฟลเดอร์โปรเจกต์

```env
HA_URL=https://your-homeassistant-url
HA_TOKEN=YOUR_LONG_LIVED_ACCESS_TOKEN
```

หมายเหตุ: ห้ามเผยแพร่ Token นี้

---

## Supported Entities

### Light

```text
light.workshop_ceiling_light_1
light.workshop_ceiling_light_2
light.workshop_ceiling_light_3
```

### Switch

```text
switch.air_compressor
```

### Fan

```text
fan.workshop_blower_fan
```

---

## Usage

### Toggle ไฟทั้ง Workshop

```bash
venv/bin/python toggle_all.py
```

### Toggle Air Compressor

```bash
venv/bin/python toggle_air_compressor.py
```

### Toggle Blower Fan

```bash
venv/bin/python toggle_blower_fan.py
```

การรันคำสั่งเดิมซ้ำจะเป็นการสลับสถานะ เปิด/ปิด

---

## Stream Deck Setup

ใช้เมนู System -> Run Command (OS)

ตัวอย่างคำสั่งสำหรับปุ่ม Toggle ไฟทั้ง Workshop

```bash
/bin/zsh -lc "cd /home/thiraphat/SynologyDrive/Programming/Stemlab && venv/bin/python toggle_all.py"
```

ข้อแนะนำในการตั้งค่า:

* ไม่เปิด Detached
* ไม่แสดง Output
* Auto run ตั้งค่าเป็น 0

---

## Notes

* หากใช้งานบน Linux หรือ macOS ต้องเรียกผ่าน shell (/bin/zsh -lc)
* หาก entity เป็น switch หรือ fan ต้องใช้ domain ให้ถูกต้อง
* หากรันผ่าน Terminal ไม่ได้ Stream Deck จะไม่สามารถสั่งงานได้

---

## License

MIT License

---
