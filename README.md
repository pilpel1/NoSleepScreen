# 💤 NoSleep - Keep Your PC Awake

<div dir="rtl">

## 🇮🇱 עברית

### מה זה?
תוכנה פשוטה שמונעת מהמחשב להיכנס למצב שינה או לכבות את המסך. שימושי במיוחד כשאתם:
- 📚 קוראים מסמך ארוך
- 📝 כותבים הערות על נייר
- 📞 בשיחת טלפון
- 🍜 אוכלים ליד המחשב

### איך משתמשים?
1. 📥 הורידו את הקובץ `NoSleep.exe` מתיקיית `dist` בפרויקט
2. ▶️ הפעילו אותו בלחיצה כפולה
3. ✨ זהו! המחשב יישאר ער
4. ⌨️ כשתרצו לסגור - לחצו Ctrl+C או סגרו את החלון
5. 🗑️ רוצים להסיר? פשוט מחקו את הקובץ

### איך זה עובד?
התוכנה לוחצת על מקש וירטואלי (F15) כל דקה, מה שגורם למחשב לחשוב שאתם פעילים. המקש הזה לא קיים ברוב המקלדות, כך שזה לא משפיע על שום דבר אחר במחשב.

</div>

## 🇺🇸 English

### What is it?
A simple utility that prevents your PC from going to sleep or turning off the screen. Especially useful when you're:
- 📚 Reading a long document
- 📝 Taking notes on paper
- 📞 On a phone call
- 🍜 Eating at your desk

### How to Use?
1. 📥 Download `NoSleep.exe` from the `dist` folder in this project
2. ▶️ Double click to run
3. ✨ That's it! Your PC will stay awake
4. ⌨️ To close - press Ctrl+C or close the window
5. 🗑️ To uninstall - simply delete the file

### How it Works?
The program simulates pressing a virtual key (F15) every minute, making your computer think you're active. This key doesn't exist on most keyboards, so it won't interfere with anything else.

## 👩‍💻 For Developers

### Requirements
- Python 3.6+
- pyautogui
- pyinstaller (for building)

### Quick Start
```bash
# Install dependencies
pip install -r requirements.txt

# Run the script
python keep_awake.py

# Build executable
pyinstaller --onefile --icon=app.ico --name NoSleep keep_awake.py
```

### Project Structure
```
├── dist/           # Compiled executable
├── keep_awake.py   # Main script
├── app.ico         # Application icon
├── requirements.txt# Python dependencies
└── README.md      # This file
```

### Want to Contribute?
This is intentionally kept simple, but feel free to enhance it! Some ideas:
- 🎨 GUI interface
- ⚙️ Configurable timer
- 📊 Activity statistics
- 🌙 Dark mode
- 🔔 System tray integration

## 📄 License
MIT License - feel free to use, modify and distribute! 