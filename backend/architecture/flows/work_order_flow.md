# Work Order Flow

## Objetivo

Gestionar el ciclo completo de fabricación de troqueles y productos relacionados desde la aprobación de una cotización hasta la entrega al cliente.

---

# 1. Creación de cotización

## Flujo

Cliente solicita fabricación o mantenimiento.

### Pasos

1. Se crea `QUOTE`
2. Se agregan `QUOTE_ITEM`
3. Se calcula total
4. Cotización queda en estado:

```txt
DRAFT
```

o

```txt
SENT
```

---

# 2. Aprobación de cotización

Cuando el cliente aprueba:

1. `QUOTE.STATUS = APPROVED`
2. `QUOTE.APPROVED_AT = now()`

Se habilita creación de `WORK_ORDER`.

---

# 3. Creación de Orden de Trabajo

Si el cliente no solicita una cotización previa no se genera `QUOTE` y se crea `WORK_ORDER` sin cotización.

Si el cliente solicita cotización previa, se genera `WORK_ORDER`

## Entidades involucradas

* WORK_ORDER
* WORK_ORDER_FILE
* WORK_ORDER_STAGE
* WORK_ORDER_MATERIAL

## Flujo

### Paso 1

Crear `WORK_ORDER`

Estados iniciales:

```txt
DRAFT
```

o

```txt
APPROVED
```

---

### Paso 2

Adjuntar archivos:

* planos
* diseños
* fotos
* especificaciones

Usando:

```txt
WORK_ORDER_FILE
```

Archivos almacenados en:

```txt
MinIO / S3
```

---

### Paso 3

Registrar materiales estimados

Tabla:

```txt
WORK_ORDER_MATERIAL
```

Campos importantes:

* ESTIMATED_QUANTITY
* EXTRA_QUANTITY

---

### Paso 4

Generar etapas automáticamente

Se crean:

1. CALADO
2. FLEJADO
3. ENCAUCHADO
4. CALIDAD

Tabla:

```txt
WORK_ORDER_STAGE
```

Estado inicial:

```txt
PENDING
```

---

# 4. Producción

## Asignación de operarios

Tabla:

```txt
WORK_ORDER_ASSIGNMENT
```

Una etapa puede tener múltiples operarios.

---

# 5. Registro de tiempos

Operarios usan tablet en planta.

Eventos:

```txt
START
PAUSE
RESUME
STOP
```

Tabla:

```txt
WORK_ORDER_STAGE_LOG
```

---

# 6. Consumo de materiales

Cuando se consume material:

1. Se actualiza:

   * WORK_ORDER_MATERIAL.CONSUMED_QUANTITY

2. Se crea:

   * STOCK_MOVEMENT

Tipo:

```txt
OUT
```

Origen:

```txt
WORK_ORDER
```

---

# 7. Compras automáticas

Si no hay stock suficiente:

1. Sistema sugiere:

   * PURCHASE_REQUEST

2. Compras genera:

   * PURCHASE_ORDER

---

# 8. Finalización

Cuando todas las etapas terminan:

```txt
WORK_ORDER.STATUS = COMPLETED
```

Campos:

```txt
COMPLETED_AT
```

---

# 9. Entrega

Se crea:

```txt
DELIVERY_NOTE
```

con:

```txt
DELIVERY_NOTE_ITEM
```

Estado OT:

```txt
DELIVERED
```

---

# 10. Integración con Siigo

Después de entregar:

1. Crear remisión en Siigo

2. Guardar:

   * SIIGO_INVOICE_ID
   * SIIGO_INVOICE_NUMBER

3. Registrar integración:

```txt
SIIGO_SYNC_LOG
```

---

# Estados recomendados WORK_ORDER

```txt
DRAFT
APPROVED
IN_PROGRESS
PAUSED
QUALITY
COMPLETED
DELIVERED
CANCELLED
```

---

# Reglas importantes

## No borrar movimientos

Nunca eliminar:

* STOCK_MOVEMENT
* WORK_ORDER_STAGE_LOG
* SIIGO_SYNC_LOG

---

## Historial de mantenimiento

Si una OT es mantenimiento:

```txt
ORIGINAL_WORK_ORDER_ID
```

debe apuntar al troquel original.

---

# Eventos futuros

## Posibles automatizaciones

* alertas de retraso
* dashboard planta
* métricas por operario
* tiempos promedio
* costos reales vs estimados
* productividad
* OT prioritarias
