#!/usr/bin/env bash
# migrate_to_neon.sh — One-shot migration: latest local backup → Neon PostgreSQL
#
# Usage:
#   export NEON_URL="postgresql://user:pass@ep-xxxx.region.aws.neon.tech/dbname?sslmode=require"
#   bash migrate_to_neon.sh
#
# Or inline:
#   NEON_URL="postgresql://..." bash migrate_to_neon.sh

set -euo pipefail

if [[ -z "${NEON_URL:-}" ]]; then
  echo "ERROR: NEON_URL is not set."
  echo "  Export it first:  export NEON_URL='postgresql://...'"
  exit 1
fi

# Find the latest backup file
BACKUP_DIR="$(cd "$(dirname "$0")/backups" && pwd)"
LATEST=$(ls -t "$BACKUP_DIR"/*.sql 2>/dev/null | head -1)

if [[ -z "$LATEST" ]]; then
  echo "ERROR: No .sql files found in $BACKUP_DIR"
  exit 1
fi

echo "----------------------------------------------"
echo "  Source backup : $LATEST"
echo "  Target        : Neon PostgreSQL"
echo "----------------------------------------------"
read -rp "Proceed? [y/N] " confirm
[[ "$confirm" =~ ^[Yy]$ ]] || { echo "Aborted."; exit 0; }

echo ""
echo "Importing backup into Neon..."
psql "$NEON_URL" < "$LATEST"

echo ""
echo "Done. Verify the import:"
echo "  psql \"\$NEON_URL\" -c \"SELECT COUNT(*) FROM project;\""
echo ""
echo "Next steps:"
echo "  1. Set DATABASE_URL in Render dashboard → Environment → NEON_URL value"
echo "  2. Update GitHub Actions secret DATABASE_URL to the same Neon URL"
echo "  3. Trigger a Render redeploy"
echo "  4. (Optional) Delete the old 'portfolio-db' in the Render dashboard"
