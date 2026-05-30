# Inventory Flow

## Objetivo

Controlar entradas y salidas de materiales usados en producción.

---

# Filosofía del sistema

La fuente de verdad es:

```txt
STOCK_MOVEMENT
```

No:

```txt
PRODUCT
```

ni:

```txt
INVENTORY_BALANCE
```

---

# 1. Entradas de inventario

Origen:

* compras
* ajustes manuales

Se crea:

```txt
STOCK_MOVEMENT
```

Tipo:

```txt
IN
```

---

# 2. Salidas de inventario

Origen:

* órdenes de trabajo
* desperdicio
* ajustes

Tipo:

```txt
OUT
```

---

# 3. Ajustes manuales

Solo administradores.

Tipo:

```txt
ADJUSTMENT
```

---

# 4. Balance actual

Tabla:

```txt
INVENTORY_BALANCE
```

Es derivada.

Puede actualizarse:

* signals
* services
* celery

---

# 5. Conversión de unidades

Ejemplo:

```txt
Compra:
1 rollo

Consumo:
3000 cm
```

Campos:

```txt
PURCHASE_UNIT
CONSUMPTION_UNIT
CONVERSION_FACTOR
```

---

# 6. Costeo promedio

Cada entrada recalcula:

```txt
AVERAGE_COST
```

Fórmula:

stock_actual * costo_actual
+
nuevo_stock * nuevo_costo

/
stock_total

````

---

# 7. Stock mínimo

Sistema alerta cuando:

```txt
CURRENT_STOCK <= MINIMUM_STOCK
````

---

# 8. Materiales por OT

Tabla:

```txt
WORK_ORDER_MATERIAL
```

Permite:

* estimado
* extra
* real consumido

---

# Reglas importantes

## No eliminar movimientos

Nunca borrar:

```txt
STOCK_MOVEMENT
```

---

## Inventario negativo

Decidir más adelante si:

* permitir
* bloquear

Para MVP:
recomendado permitir con warning.
