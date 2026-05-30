# Database Conventions

## IDs

* All tables use UUID primary keys.

## Timestamps

* Transactional tables should contain CREATED_AT.
* Mutable entities should contain UPDATED_AT.

## Inventory

* STOCK_MOVEMENT is the source of truth.
* INVENTORY_BALANCE is only a snapshot.

## Work Orders

* Manufacturing history is preserved through ORIGINAL_WORK_ORDER_ID.

## Files

* Files are stored in MinIO/S3.
* OBJECT_KEY stores the bucket path.

## Naming

* Table names use singular uppercase.
* Foreign keys use *_ID suffix.
