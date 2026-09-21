import logging
import os
from datetime import datetime

# إنشاء اسم الملف باستخدام الوقت والتاريخ الحالي
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# تحديد مسار مجلد logs داخل المشروع
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# إنشاء المجلد إذا لم يكن موجوداً
os.makedirs(logs_path, exist_ok=True)

# المسار الكامل لملف الـ log
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# ضبط إعدادات الـ Logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

