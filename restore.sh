#!/bin/bash
set -e

echo "Восстановление базы данных из дампа..."
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -f /data/dump_file.sql
echo "Готово!"
