# production_tracking_flow.md

# Objetivo

Gestionar producción en tiempo real.

---

# Flujo principal

WORK_ORDER
→ WORK_ORDER_STAGE
→ WORK_ORDER_STAGE_LOG

---

# Estados etapa

```txt id="lxbyiu"
PENDING
IN_PROGRESS
PAUSED
COMPLETED
```

---

# Eventos

## START

Inicia cronómetro.

## PAUSE

Detiene temporalmente.

## RESUME

Continúa tiempo.

## STOP

Finaliza etapa.

---

# Reglas

## Múltiples operarios

Permitido.

Tabla:

```txt id="4tbdvf"
WORK_ORDER_ASSIGNMENT
```

---

# Cálculo tiempo

TOTAL_TIME:

```txt id="yjlwmz"
SUM(STOP - START)
- pausas
```

---

# Flujo automático

Cuando etapa termina:

* siguiente etapa → PENDING

---

# Dashboard planta

Mostrar:

* etapa actual
* operarios
* tiempo real
* prioridad
* retrasos

---

# Futuro

* códigos QR
* tablets
* pantallas TV
* métricas productividad
