# authentication_authorization_flow.md

# Objetivo

Controlar autenticación, autorización y acceso al sistema.

---

# Roles iniciales

## ADMIN

Acceso total.

## OFFICE

* cotizaciones
* compras
* clientes
* remisiones

## PLANT

* tablero planta
* iniciar etapas
* pausar
* finalizar

---

# Login

## Flujo

1. Usuario ingresa email/password
2. Validar credenciales
3. Generar JWT/session
4. Registrar AUDIT_LOG

---

# Permisos importantes

## WORK_ORDER

* create
* approve
* edit
* cancel

## INVENTORY

* view
* adjust

## SIIGO

* sync
* retry

---

# Middleware

## Requerido

* authentication
* permission checking
* audit logging

---

# Reglas

## PLANT

No puede:

* editar costos
* modificar compras
* sincronizar Siigo

---

# Futuro

* RBAC granular
* permisos dinámicos
* SSO
* MFA
