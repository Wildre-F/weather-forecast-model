```
██╗    ██╗███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██║  ██║   ██║   ██║  ██║███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
██████╗ ██████╗ ███████╗██████╗ ██╗ ██████╗████████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔══██╗██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
██████╔╝██████╔╝█████╗  ██║  ██║██║██║        ██║   ██║   ██║██████╔╝
██╔═══╝ ██╔══██╗██╔══╝  ██║  ██║██║██║        ██║   ██║   ██║██╔══██╗
██║     ██║  ██║███████╗██████╔╝██║╚██████╗   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
```

<div align="center">

![Status](https://img.shields.io/badge/STATUS-COMPLETE-1d9e75?style=flat-square)
![ML](https://img.shields.io/badge/TYPE-MACHINE%20LEARNING-5c5fd4?style=flat-square)
![Dataset](https://img.shields.io/badge/DATASET-KAGGLE%20%7C%20ECCC-ff69b4?style=flat-square)
![Year](https://img.shields.io/badge/DATA%20YEAR-2012-7f77dd?style=flat-square)

```
> SYSTEM ONLINE... LOADING WEATHER PREDICTION MODULE... OK
> CONNECTING TO ATMOSPHERIC DATA FEED... OK  
> ML MODELS INITIALISED... OK
> READY.
```

</div>

---

```
╔══════════════════════════════════════════════╗
║              // MISSION BRIEF                ║
╚══════════════════════════════════════════════╝
```

Weather prediction plays a critical role in industries like **agriculture**, **aviation**, and **transportation** — yet many existing systems are too complex for quick, practical decision-making.

**WeatherPredictor** is a machine learning system that predicts weather conditions from atmospheric data and presents results through a simple, accessible web application. Users input atmospheric values and receive **real-time predictions** for:

- 🌡️ Temperature *(regression)*
- 🌧️ Rain *(classification)*
- ❄️ Snow *(classification)*
- 👁️ Visibility *(classification)*

---

```
╔══════════════════════════════════════════════╗
║              // BUILT WITH                   ║
╚══════════════════════════════════════════════╝
```

<div align="center">
  <img src="https://skillicons.dev/icons?i=python,flask,html,css,js" />
</div>

**Additional Libraries**
```
> scikit-learn   — ML model training & evaluation
> pandas         — data manipulation & preprocessing  
> numpy          — numerical computations
> matplotlib     — data visualisation
> seaborn        — statistical plots
> kaggle         — dataset source
```

---

```
╔══════════════════════════════════════════════╗
║              // DATA TERMINAL                ║
╚══════════════════════════════════════════════╝
```

| Parameter | Value |
|---|---|
| 📍 **Source** | Kaggle — Environment & Climate Change Canada (ECCC) |
| 🛫 **Location** | Toronto Pearson Airport |
| 📅 **Period** | 2012 (Leap Year — 366 days) |
| 📊 **Records** | 8,784 hourly observations |
| 🔢 **Original Features** | Temperature, Humidity, Wind Speed, Pressure, Visibility, Weather Description |
| ⚙️ **Engineered Features** | Time-based variables, encoded weather conditions |

---

```
╔══════════════════════════════════════════════╗
║              // ML MODULES                   ║
╚══════════════════════════════════════════════╝
```

| Target | Task | Notes |
|---|---|---|
| 🌡️ **Temperature** | Regression | Continuous value prediction |
| 🌧️ **Rain** | Classification | Binary — rain / no rain |
| ❄️ **Snow** | Classification | Class imbalance challenge |
| 👁️ **Visibility** | Classification | Class imbalance challenge |

> ⚠️ **Key Challenge:** Significant class imbalance detected for snow and visibility conditions. Addressed during preprocessing and model tuning.

---

```
╔══════════════════════════════════════════════╗
║           // SYSTEM OBSERVATIONS             ║
╚══════════════════════════════════════════════╝
```

During initial data exploration the following patterns were identified:

- 📈 Seasonal temperature trends clearly visible across the year
- 💧 High humidity strongly correlated with rainfall events
- ❄️ Snow and low visibility conditions underrepresented in dataset
- 🔗 Pressure and wind speed show predictive relationships with weather changes

---

```
╔══════════════════════════════════════════════╗
║            // LAUNCH SEQUENCE                ║
╚══════════════════════════════════════════════╝
```

```bash
# Clone the repo
git clone https://github.com/Wildre-F/WeatherPredictor.git

# Install dependencies
pip install -r requirements.txt

# Launch web application
python app.py

# Navigate to
http://localhost:5000
```

---

```
╔══════════════════════════════════════════════╗
║              // COLLABORATORS                ║
╚══════════════════════════════════════════════╝
```

> Built as part of the Machine Learning module at **Belgium Campus ITversity**.

---

<div align="center">

```
> WEATHER PREDICTION SYSTEM v1.0
> ALL SYSTEMS NOMINAL
> SIGNING OFF...
```

</div>
