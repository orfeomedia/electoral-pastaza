# 🗳️ Electoral Pastaza 2023-2025

## Análisis Electoral Completo de la Provincia de Pastaza

Sistema de análisis electoral con datos oficiales del CNE Ecuador.

---

## 📊 **Datos Incluidos**

### **1. Elecciones Seccionales 2023**
- ✅ Prefecto Provincial (André Granda - 17,426 votos)
- ✅ Alcaldes de 4 cantones (Pastaza, Mera, Santa Clara, Arajuno)
- ✅ Concejales Urbanos y Rurales
- ✅ Vocales de Juntas Parroquiales

### **2. Asambleístas Provinciales**
**2023:**
- Construye: 21,665 votos
- Unidos por Pastaza: 16,295 votos
- Revolución Ciudadana: 14,560 votos
- Movimiento Semilla: 11,837 votos

**2025:**
- ADN: 53,383 votos (+730%)
- Revolución Ciudadana: 27,053 votos
- ADN-Semilla: 16,570 votos
- Pachakutik: 15,586 votos

---

## 🚀 **Instalación y Uso**

### **Opción A: Streamlit Cloud (Recomendado)**

1. **Crear repositorio en GitHub:**
```
Nombre: electoral-pastaza
Tipo: Público
```

2. **Subir estos 4 archivos:**
- `app.py` (renombrar app_pastaza_final.py)
- `requirements.txt` (renombrar requirements_final.txt)
- `README.md` (este archivo)
- `Resultados-electorales-2023.csv`
- `Primera-vuelta_2023.csv`
- `Primera-vuelta_2025.csv`
- `Candidatos-2023.csv`

3. **Deploy en Streamlit:**
- https://share.streamlit.io/
- New app
- Repository: tu-usuario/electoral-pastaza
- Branch: main
- Main file: app.py

### **Opción B: Local**

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecutar app
streamlit run app.py
```

---

## 📁 **Estructura de Archivos**

```
electoral-pastaza/
├── app.py                               # App principal
├── requirements.txt                      # Dependencias
├── README.md                            # Documentación
├── Resultados-electorales-2023.csv      # Seccionales 2023
├── Primera-vuelta_2023.csv              # Asambleístas 2023
├── Primera-vuelta_2025.csv              # Asambleístas 2025
└── Candidatos-2023.csv                  # Info candidatos
```

---

## ✨ **Características**

### **Dashboard General**
- Resumen ejecutivo
- Métricas clave
- Acceso rápido

### **Seccionales 2023**
- Resultados de Prefecto
- Ganador destacado
- Gráficos interactivos
- Rankings completos

### **Asambleístas**
- Análisis 2023 y 2025
- Top 10 partidos
- Gráficos de barras

### **Comparación Temporal**
- Tabla comparativa 2023 vs 2025
- Variación porcentual
- Identificación de tendencias
- Gráficos lado a lado

---

## 📊 **Resultados Principales**

### **Prefecto 2023**
🏆 **André Granda** (¡Ánimo Pastaza!) - 17,426 votos

### **Asambleístas - Variación 2023→2025**
- **ADN:** +730% (de 6,445 a 53,383)
- **Pachakutik:** +133% (de 6,700 a 15,586)
- **Construye:** -96% (de 21,665 a 881)

---

## 🎯 **Uso de la App**

### **1. Dashboard General**
Vista general con métricas principales

### **2. Seccionales 2023**
- Ver resultados de Prefecto
- Explorar alcaldes por cantón
- Analizar concejales

### **3. Asambleístas**
- Comparar resultados 2023 y 2025
- Ver evolución de partidos
- Identificar tendencias

### **4. Comparación**
- Tabla con variaciones
- Gráficos comparativos
- Análisis de crecimiento

---

## 🔧 **Troubleshooting**

### **Error: File not found**
✅ Verificar que TODOS los CSV estén en la raíz del repositorio

### **Error: ModuleNotFoundError**
✅ Verificar requirements.txt en la raíz

### **App muy lenta**
✅ Normal en primera carga (226K+ registros)

---

## 📞 **Contacto**

**Datos oficiales:** CNE Ecuador  
**Teléfono CNE:** (593-2) 381-5410  
**Web:** https://www.cne.gob.ec

---

## 📄 **Licencia**

Datos públicos del CNE Ecuador  
Aplicación de análisis electoral transparente

---

**Desarrollado para análisis electoral en Pastaza** 🇪🇨  
*Última actualización: Febrero 2026*
