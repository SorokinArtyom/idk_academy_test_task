#!/bin/bash
set -e

# Проверяем, существует ли база
RESULT=$(psql -U "$POSTGRES_USER" -tAc "SELECT 1 FROM pg_database WHERE datname='$POSTGRES_DB'")
if [ "$RESULT" != "1" ]; then
    echo "Создаём базу $POSTGRES_DB"
    createdb -U "$POSTGRES_USER" "$POSTGRES_DB"
fi

# Восстанавливаем дамп через pg_restore
echo "Восстанавливаем дамп..."
pg_restore -U "$POSTGRES_USER" -d "$POSTGRES_DB" --clean --if-exists /docker-entrypoint-initdb.d/dump_file.dump

echo "Восстановление завершено"
