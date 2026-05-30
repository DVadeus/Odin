# Siigo Sync Flow

## Objetivo

Sincronizar remisiones y facturación entre Odin y Siigo.

---

# Filosofía

Odin:

* operación
* producción
* inventario

Siigo:

* facturación
* contabilidad
* DIAN

---

# 1. Creación de remisión

Cuando OT se entrega:

1. Crear:

   ```txt
   DELIVERY_NOTE
   ```

2. Crear:

   ```txt
   DELIVERY_NOTE_ITEM
   ```

Estado:

```txt
PENDING
```

---

# 2. Envío a Siigo

Proceso recomendado:

```txt
Celery background task
```

---

# 3. Payload

Enviar:

* cliente
* productos
* cantidades
* precios
* observaciones

---

# 4. Respuesta Siigo

Guardar:

```txt
SIIGO_INVOICE_ID
SIIGO_INVOICE_NUMBER
```

---

# 5. Log de integración

Registrar request/response:

```txt
SIIGO_SYNC_LOG
```

Estados:

```txt
PENDING
SUCCESS
ERROR
RETRY
```

---

# 6. Reintentos

Si falla:

* retry automático
* exponential backoff

---

# 7. Validaciones

Antes de sincronizar:

* cliente debe existir
* precio válido
* OT entregada
* remisión activa

---

# 8. Estrategia recomendada

Nunca enviar directamente desde request HTTP.

Usar:

```txt
Celery + Redis
```

---

# 9. Flujo recomendado

```txt
DELIVERY_NOTE
→ Celery Task
→ API Siigo
→ SIIGO_SYNC_LOG
→ Actualizar DELIVERY_NOTE
```

---

# 10. Futuro

Posibles integraciones:

* facturas
* notas crédito
* clientes
* pagos
* inventario
