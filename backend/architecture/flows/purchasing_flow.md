# Purchasing Flow

## Objetivo

Gestionar compras de materiales para producción.

---

# 1. Detección de faltante

Durante preparación de OT:

Sistema calcula:

```txt
STOCK ACTUAL
vs
MATERIAL REQUERIDO
```

Si no alcanza:

* sugerir compra

---

# 2. Solicitud de compra

Se crea:

```txt
PURCHASE_REQUEST
```

Estado inicial:

```txt
PENDING
```

Items:

```txt
PURCHASE_REQUEST_ITEM
```

---

# 3. Aprobación

Compras revisa:

* prioridad
* urgencia
* proveedor

Estados:

```txt
APPROVED
ORDERED
CANCELLED
```

---

# 4. Generación de orden de compra

Se crea:

```txt
PURCHASE_ORDER
```

Items:

```txt
PURCHASE_ORDER_ITEM
```

Relación:

```txt
PURCHASE_ORDER_ITEM
→ PURCHASE_REQUEST_ITEM
```

---

# 5. Recepción parcial

Campo:

```txt
RECEIVED_QUANTITY
```

permite:

* recepciones parciales
* backorders
* compras incompletas

---

# 6. Entrada a inventario

Cuando llega material:

Se crea:

```txt
STOCK_MOVEMENT
```

Tipo:

```txt
IN
```

Origen:

```txt
PURCHASE
```

---

# 7. Actualización de costos

El costo de compra:

```txt
PURCHASE_ORDER_ITEM.UNIT_COST
```

alimenta:

```txt
STOCK_MOVEMENT.UNIT_COST
```

y recalcula:

```txt
PRODUCT.AVERAGE_COST
```

---

# Estados PURCHASE_ORDER

```txt
DRAFT
SENT
RECEIVED
CANCELLED
```

---

# Estados PURCHASE_REQUEST

```txt
DRAFT
PENDING
APPROVED
PARTIAL
ORDERED
CLOSED
CANCELLED
```

---

# Reglas importantes

## Nunca editar históricos

No modificar:

* STOCK_MOVEMENT
* costos históricos

---

## Recepciones parciales

Permitidas.

Ejemplo:

```txt
Solicitado: 100
Recibido: 60
Pendiente: 40
```
