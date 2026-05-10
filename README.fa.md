# 🦠 شبیه‌ساز اپیدمی SIR

[![PyPI version](https://badge.fury.io/py/sir-epidemic.svg)](https://pypi.org/project/sir-epidemic/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/sir-epidemic)](https://pypi.org/project/sir-epidemic/)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Tests](https://github.com/miladrezanezhad/sir_simulator/actions/workflows/test.yml/badge.svg)](https://github.com/miladrezanezhad/sir_simulator/actions/workflows/test.yml)
[![Security](https://img.shields.io/badge/security-tests-brightgreen)](SECURITY_TESTS.md)
[![Code Coverage](https://img.shields.io/badge/coverage-51%25-orange)](coverage_html_report/index.html)
[![GitHub stars](https://img.shields.io/github/stars/miladrezanezhad/sir_simulator)](https://github.com/miladrezanezhad/sir_simulator/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/miladrezanezhad/sir_simulator)](https://github.com/miladrezanezhad/sir_simulator/network)
[![GitHub issues](https://img.shields.io/github/issues/miladrezanezhad/sir_simulator)](https://github.com/miladrezanezhad/sir_simulator/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/miladrezanezhad/sir_simulator)](https://github.com/miladrezanezhad/sir_simulator/commits/main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Streamlit](https://img.shields.io/badge/streamlit-app-red)](https://streamlit.io)
[![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey)]()

**یک مجموعه کامل مدل‌سازی اپیدمی با ۶ ویژگی یکپارچه**

---

## 📋 فهرست مطالب

- [نمای کلی](#-نمای-کلی)
- [ویژگی‌ها](#-ویژگی‌ها)
- [نصب](#-نصب)
- [شروع سریع](#-شروع-سریع)
- [مستندات](#-مستندات)
- [ساختار پروژه](#-ساختار-پروژه)
- [راهنمای استفاده](#-راهنمای-استفاده)
- [تست](#-تست)
- [امنیت](#-امنیت)
- [تصاویر](#-تصاویر)
- [مشارکت](#-مشارکت)
- [مجوز](#-مجوز)

---

<div dir="rtl" align="center">
  <br>
  <strong style="font-size: 1.2rem;">🌐 زبان‌ها:</strong>
  <br><br>
  <strong style="font-size: 1.1rem;">
    <a href="README.md" style="text-decoration: none;">🇬🇧 انگلیسی</a> &nbsp;|&nbsp;
    <a href="README.fa.md" style="text-decoration: none;">🇮🇷 فارسی</a>
  </strong>
  <br><br>
</div>

---

## 🔭 نمای کلی

**شبیه‌ساز اپیدمی SIR** یک مجموعه جامع مدل‌سازی اپیدمی است که مدل‌های کلاسیک compartments را با یادگیری ماشین مدرن ترکیب می‌کند. این ابزار به محققان، دانشجویان و متخصصان سلامت عمومی امکان شبیه‌سازی، تحلیل و پیش‌بینی دینامیک اپیدمی را می‌دهد.

| قابلیت | توضیحات |
|:---|:---|
| 📈 **مدل SIR** | دینامیک پایه Susceptible-Infected-Recovered |
| 🧬 **مدل SEIR** | افزودن بخش نهفتگی/دوره کمون |
| 🌐 **شبیه‌سازی شبکه** | گسترش اخبار جعلی در شبکه‌های اجتماعی |
| 🎯 **بهینه‌سازی پارامترها** | تطبیق مدل‌ها با داده‌های واقعی |
| 🤖 **پیش‌بینی با ML** | پیش‌بینی موارد آینده با XGBoost/Random Forest |
| ⚖️ **مقایسه سناریوها** | ارزیابی قرنطینه در مقابل واکسیناسیون |

---

## ✨ ویژگی‌ها

### مدل‌های اصلی
- ✅ مدل SIR با حل‌کننده ODE
- ✅ مدل SEIR با بخش نهفتگی
- ✅ تأیید بقای جمعیت
- ✅ پارامترهای شبیه‌سازی قابل تنظیم

### شبیه‌سازی شبکه
- ✅ شبکه بدون مقیاس (Barabási-Albert)
- ✅ شبکه جهان کوچک (Watts-Strogatz)
- ✅ شبکه تصادفی (Erdos-Renyi)
- ✅ شبیه‌سازی گسترش SIR در شبکه‌های اجتماعی
- ✅ محاسبه آمار شبکه

### ویژگی‌های پیشرفته
- ✅ بهینه‌سازی پارامترها با استفاده از تکامل تفاضلی
- ✅ برازش منحنی برای داده‌های واقعی اپیدمی
- ✅ پیش‌بینی با ML با استفاده از Random Forest و XGBoost
- ✅ مقایسه سناریوها (پایه، قرنطینه، واکسیناسیون، ترکیبی)

### رابط کاربری
- ✅ داشبورد وب Streamlit
- ✅ رابط خط فرمان (CLI)
- ✅ سیستم منوی تعاملی
- ✅ قابلیت خروجی CSV

### تست و امنیت
- ✅ بیش از ۳۵ تست واحد
- ✅ ۲۲ تست امنیتی (DoS، حافظه، یونیکد، XSS)
- ✅ GitHub Actions CI/CD
- ✅ هاوک‌های پیش از ارسال برای کیفیت کد

---

## 🚀 نصب

### پیش‌نیازها
- پایتون ۳.۸ یا بالاتر
- مدیر بسته pip

### نصب از PyPI (توصیه می‌شود)

```bash
pip install sir-epidemic
```

### نصب از کد منبع (برای توسعه)

```bash
git clone https://github.com/miladrezanezhad/sir_simulator.git
cd sir_simulator
pip install -e .
```

### تأیید نصب

```bash
python -c "import sir_simulator; print('✅ موفق!')"
```

---

## 🎮 شروع سریع

### ۱️⃣ اجرای داشبورد Streamlit (توصیه می‌شود)

```bash
streamlit run src/sir_simulator/user_interface/app.py
```

سپس در مرورگر خود آدرس http://localhost:8501 را باز کنید.

### ۲️⃣ اجرای CLI

```bash
sir-simulator --beta 0.5 --gamma 0.2 --tmax 100
```

### ۳️⃣ اجرای منوی تعاملی

```bash
python main.py
```

### ۴️⃣ اجرای تمام تست‌ها

```bash
python run_all_tests.py
python -m unittest discover tests/security
```

---

## 📚 مستندات

### ویکی کامل

برای آموزش‌های دقیق، مرجع API و سوالات متداول، به [ویکی گیت‌هاب](https://github.com/miladrezanezhad/sir_simulator/wiki) ما مراجعه کنید:

| صفحه ویکی | توضیحات |
|:---|:---|
| [🏠 صفحه اصلی](https://github.com/miladrezanezhad/sir_simulator/wiki) | صفحه اصلی ویکی |
| [🚀 شروع به کار](https://github.com/miladrezanezhad/sir_simulator/wiki/Getting-Started) | نصب و گام‌های اولیه |
| [📈 آموزش مدل SIR](https://github.com/miladrezanezhad/sir_simulator/wiki/SIR-Model-Tutorial) | راهنمای کامل مدل SIR |
| [🧬 آموزش مدل SEIR](https://github.com/miladrezanezhad/sir_simulator/wiki/SEIR-Model-Tutorial) | راهنمای کامل مدل SEIR |
| [🌐 آموزش شبیه‌سازی شبکه](https://github.com/miladrezanezhad/sir_simulator/wiki/Network-Simulation-Tutorial) | راهنمای گسترش در شبکه اجتماعی |
| [🤖 آموزش پیش‌بینی ML](https://github.com/miladrezanezhad/sir_simulator/wiki/ML-Prediction-Tutorial) | پیش‌بینی با یادگیری ماشین |
| [⚖️ آموزش مقایسه سناریوها](https://github.com/miladrezanezhad/sir_simulator/wiki/Scenario-Comparison-Tutorial) | استراتژی‌های مداخله |
| [❓ سوالات متداول](https://github.com/miladrezanezhad/sir_simulator/wiki/FAQ) | سوالات متداول |
| [📚 مرجع API](https://github.com/miladrezanezhad/sir_simulator/wiki/API-Reference) | مستندات کامل توابع |
| [🤝 راهنمای مشارکت](https://github.com/miladrezanezhad/sir_simulator/wiki/Contributing-Guide) | نحوه مشارکت |

### مستندات محلی

| فایل | توضیحات |
|:---|:---|
| [TESTING.md](TESTING.md) | راهنمای کامل تست |
| [SECURITY_TESTS.md](SECURITY_TESTS.md) | مستندات تست امنیتی |
| [SECURITY.md](SECURITY.md) | سیاست امنیتی |
| [CONTRIBUTING.md](CONTRIBUTING.md) | دستورالعمل مشارکت |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | رفتار حرفه‌ای |
| [CHANGELOG.md](CHANGELOG.md) | تاریخچه نسخه‌ها |

---

## 📁 ساختار پروژه

```
sir_simulator/
│
├── src/sir_simulator/          # کد منبع
│   ├── core_models/            # مدل‌های اصلی ریاضی
│   │   ├── sir_model.py        # پیاده‌سازی SIR پایه
│   │   ├── seir_model.py       # SEIR با بخش نهفتگی
│   │   └── network_model.py    # شبیه‌سازی گسترش در شبکه اجتماعی
│   │
│   ├── advanced_features/      # قابلیت‌های پیشرفته
│   │   ├── parameter_optimization.py  # برازش منحنی
│   │   ├── ml_prediction.py           # پیش‌بینی ML
│   │   └── scenario_comparison.py     # تحلیل مداخله
│   │
│   └── user_interface/         # برنامه‌های رابط کاربری
│       ├── app.py              # داشبورد Streamlit
│       └── cli.py              # رابط خط فرمان
│
├── tests/                      # مجموعه تست (بیش از ۵۷ تست)
│   ├── test_seir.py            # تست‌های مدل SEIR
│   ├── test_network.py         # تست‌های شبیه‌سازی شبکه
│   ├── test_optimization.py    # تست‌های بهینه‌سازی پارامتر
│   ├── test_ml.py              # تست‌های پیش‌بینی ML
│   ├── test_scenarios.py       # تست‌های مقایسه سناریوها
│   └── security/               # مجموعه تست امنیت
│       ├── test_dos_attack.py
│       ├── test_memory_exhaustion.py
│       ├── test_unicode_attacks.py
│       └── test_xss_prevention.py
│
├── docs/                       # مستندات
│   └── notebook.ipynb          # نوت‌بوک آموزشی جیوپایتر
│
├── screenshots/                # تصاویر برنامه (۷ تصویر)
│
├── .github/workflows/          # خطوط لوله CI/CD
│   ├── test.yml                # خودکارسازی تست
│   └── security.yml            # خط لوله اسکن امنیت
│
├── README.md                   # این فایل
├── TESTING.md                  # راهنمای تست
├── SECURITY_TESTS.md           # راهنمای تست امنیت
├── SECURITY.md                 # سیاست امنیت
├── CONTRIBUTING.md             # راهنمای مشارکت
├── CODE_OF_CONDUCT.md          # رفتار حرفه‌ای
├── CHANGELOG.md                # تاریخچه نسخه‌ها
├── LICENSE                     # مجوز MIT
├── pyproject.toml              # پیکربندی پروژه
├── requirements.txt            # وابستگی‌های پایتون
├── requirements_dev.txt        # وابستگی‌های توسعه
├── Makefile                    # خودکارسازی وظایف رایج
├── main.py                     # منوی تعاملی
└── run_all_tests.py            # اجراکننده اصلی تست
```

---

## 📊 راهنمای استفاده

### ۱. مدل SIR

```python
from sir_simulator.core_models.sir_model import run_sir_simulation

df = run_sir_simulation(
    beta=0.5, gamma=0.2,
    S0=990, I0=10, R0=0,
    t_max=100, steps=500
)
```

### ۲. مدل SEIR

```python
from sir_simulator.core_models.seir_model import run_seir_simulation

df = run_seir_simulation(
    beta=0.5, sigma=0.2, gamma=0.1,
    S0=990, E0=5, I0=5, R0=0,
    t_max=100, steps=500
)
```

### ۳. شبیه‌سازی شبکه

```python
from sir_simulator.core_models.network_model import SocialNetworkSimulator

sim = SocialNetworkSimulator(num_nodes=200, network_type='scale_free')
df = sim.simulate_spread(transmission_prob=0.4, recovery_prob=0.1)
```

### ۴. بهینه‌سازی پارامترها

```python
from sir_simulator.advanced_features.parameter_optimization import ParameterOptimizer

optimizer = ParameterOptimizer(model_type='sir')
results = optimizer.fit(observed_data, t, [990, 10, 0])
print(f"β={results['beta']:.3f}, γ={results['gamma']:.3f}, R0={results['R0']:.3f}")
```

### ۵. پیش‌بینی با یادگیری ماشین

```python
from sir_simulator.advanced_features.ml_prediction import EpidemicPredictor

predictor = EpidemicPredictor(model_type='random_forest')
metrics, predictions, _ = predictor.train(historical_data)
future = predictor.predict_future(historical_data, days=30)
```

### ۶. مقایسه سناریوها

```python
from sir_simulator.advanced_features.scenario_comparison import ScenarioComparator

comp = ScenarioComparator(beta=0.25, gamma=0.1)
scenarios, metrics = comp.compare_all_scenarios(days=120)
print(metrics)
```

---

## 🧪 تست

### اجرای تمام تست‌ها

```bash
python run_all_tests.py
python -m unittest discover tests/security
```

### پوشش تست

| ماژول | تعداد تست | وضعیت |
|:---|:---:|:---:|
| مدل SEIR | ۷ | ✅ |
| مدل شبکه | ۱۰ | ✅ |
| بهینه‌سازی پارامتر | ۶ | ✅ |
| پیش‌بینی ML | ۲ (فعال) + ۲ (غیرفعال) | ✅ |
| مقایسه سناریوها | ۸ | ✅ |
| امنیت (DoS، حافظه، یونیکد، XSS) | ۲۲ | ✅ |
| **مجموع** | **۵۷** | **✅ همه با موفقیت** |

### اجرای تست‌های جداگانه

```bash
python tests/test_seir.py
python tests/test_network.py
python tests/test_optimization.py
python tests/test_ml.py
python tests/test_scenarios.py
python tests/security/test_dos_attack.py
```

برای مستندات دقیق تست، به [TESTING.md](TESTING.md) مراجعه کنید.

---

## 🔒 امنیت

این پروژه شامل تست امنیت جامع است:

| دسته تست | تعداد تست | وضعیت |
|:---|:---:|:---:|
| جلوگیری از حملات DoS | ۵ | ✅ |
| محافظت در برابر خستگی حافظه | ۴ | ✅ |
| مقابله با حملات یونیکد/UTF-8 | ۶ | ✅ |
| جلوگیری از XSS برای Streamlit | ۷ | ✅ |
| **مجموع** | **۲۲** | **✅ همه با موفقیت** |

همه تست‌های امنیتی با موفقیت عبور کرده و هیچ آسیب‌پذیری تشخیص داده نشده است.

برای مسائل امنیتی، لطفاً به [SECURITY.md](SECURITY.md) مراجعه کنید.

---

## 📸 تصاویر

| مدل SIR | مدل SEIR |
|:---:|:---:|
| ![SIR](screenshots/SIR%20Epidemic%20Model.png) | ![SEIR](screenshots/SEIR%20Model%20with%20Exposed%20Compartment.png) |

| شبیه‌سازی شبکه | بهینه‌سازی پارامتر |
|:---:|:---:|
| ![Network](screenshots/Fake%20News%20Spread%20on%20Social%20Network.png) | ![Optimization](screenshots/Parameter%20Optimization.png) |

| پیش‌بینی ML | مقایسه سناریوها |
|:---:|:---:|
| ![ML](screenshots/Machine%20Learning%20Prediction.png) | ![Scenarios](screenshots/Scenario%20Comparison.png) |

### 📊 داشبورد Streamlit

![Dashboard](screenshots/dashboard.png)

---

## 🤝 مشارکت

مشارکت خوش آمد است! لطفاً برای دستورالعمل‌ها به [CONTRIBUTING.md](CONTRIBUTING.md) مراجعه کنید.

### مراحل سریع

۱. مخزن را فورک کنید
۲. یک شاخه ویژگی ایجاد کنید
۳. تغییرات خود را اعمال کنید
۴. تست‌ها را اجرا کنید: `python run_all_tests.py`
۵. یک درخواست کشش ارسال کنید

### راه‌اندازی توسعه

```bash
git clone https://github.com/YOUR_USERNAME/sir_simulator.git
cd sir_simulator
pip install -e .
pip install -r requirements_dev.txt
pre-commit install
```

---

## 📄 مجوز

این پروژه تحت **مجوز MIT** است - برای جزئیات به فایل [LICENSE](LICENSE) مراجعه کنید.

---

## 🙏 قدردانی

- مدل‌های کلاسیک SIR/SEIR از تئوری Kermack-McKendrick
- الگوریتم‌های علوم شبکه از کتابخانه NetworkX
- مدل‌های یادگیری ماشین از scikit-learn و XGBoost
- Streamlit برای چارچوب داشبورد تعاملی

---

## 📞 تماس و پشتیبانی

| کانال | لینک |
|:---|:---|
| **مسائل گیت‌هاب** | [گزارش باگ](https://github.com/miladrezanezhad/sir_simulator/issues) |
| **بحث‌های گیت‌هاب** | [پرسش سوال](https://github.com/miladrezanezhad/sir_simulator/discussions) |
| **ایمیل** | miladvf2014@gmail.com |
| **PyPI** | [sir-epidemic](https://pypi.org/project/sir-epidemic/) |

---

## ⭐ به پروژه ستاره دهید

اگر این پروژه را مفید می‌دانید، لطفاً در گیت‌هاب به آن **ستاره** دهید!

[![GitHub stars](https://img.shields.io/github/stars/miladrezanezhad/sir_simulator?style=social)](https://github.com/miladrezanezhad/sir_simulator/stargazers)

---

**ساخته شده با ❤️ برای مدل‌سازی اپیدمی و تحقیقات سلامت عمومی**

[⬆ بازگشت به بالا](#-شبیه‌ساز-اپیدمی-sir)
