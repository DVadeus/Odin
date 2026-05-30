# quotation_flow.md

# Objetivo

Gestionar cotizaciones comerciales.

---

# Estados

```txt id="0ld6hy"
DRAFT
SENT
APPROVED
REJECTED
EXPIRED
```

---

# Flujo

## 1. Crear QUOTE

Agregar:

* cliente
* items
* precio
* notas

---

# 2. Enviar

Estado:

```txt id="4t1m3q"
SENT
```

---

# 3. Aprobar

Cliente aprueba.

Actualizar:

```txt id="7nq8i8"
APPROVED
APPROVED_AT
```

---

# 4. Crear WORK_ORDER

# Reglas

## Precio final

WORK_ORDER.UNIT_PRICE:

1. usar QUOTE
2. permitir override manual

---

# Expiración

Si VALID_UNTIL expira:

```txt id="mdu8qs"
EXPIRED
```

---

# Futuro

* PDF automático
* firma digital
* email cliente
