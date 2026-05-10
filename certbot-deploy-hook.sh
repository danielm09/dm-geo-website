#!/bin/sh
set -eu

# certbot provides RENEWED_LINEAGE to deploy hooks
HOST="dm-geo.com"
LINEAGE="$(basename "${RENEWED_LINEAGE:?RENEWED_LINEAGE must be set}")"

echo "[certbot-hook] HOST=$HOST LINEAGE=$LINEAGE"

# Keep nginx paths stable even if certbot uses suffixed lineages
if [ "${LINEAGE}" != "${HOST}" ]; then
  echo "[certbot-hook] Creating stable symlinks: live/$HOST -> $LINEAGE"
  mkdir -p "/etc/letsencrypt/live/${HOST}"
  ln -sfn "../${LINEAGE}/fullchain.pem" "/etc/letsencrypt/live/${HOST}/fullchain.pem"
  ln -sfn "../${LINEAGE}/privkey.pem"   "/etc/letsencrypt/live/${HOST}/privkey.pem"
fi

chmod 755 /etc/letsencrypt /etc/letsencrypt/live /etc/letsencrypt/archive 2>/dev/null || true

# Per-host dirs: owner+group read/enter (gid 0 = root group, nginx uses gid 0)
find /etc/letsencrypt/live    -maxdepth 1 -type d -name "${HOST}*" -exec chmod 750 {} +
find /etc/letsencrypt/archive -maxdepth 1 -type d -name "${HOST}*" -exec chmod 750 {} +

# Public cert files: readable by all
find /etc/letsencrypt/archive -name "fullchain*.pem"  -exec chmod 644 {} +
find /etc/letsencrypt/archive -name "chain*.pem"      -exec chmod 644 {} +
find /etc/letsencrypt/archive -name "cert*.pem"       -exec chmod 644 {} +
find /etc/letsencrypt/live    -name "fullchain.pem"   -exec chmod 644 {} +
find /etc/letsencrypt/live    -name "chain.pem"       -exec chmod 644 {} +
find /etc/letsencrypt/live    -name "cert.pem"        -exec chmod 644 {} +

# Private keys: readable only by owner + group (gid 0 = root group, nginx uses gid 0)
find /etc/letsencrypt -type f -name "privkey*.pem" -exec chmod 0640 {} +

# Signal nginx to reload its TLS config
touch /var/www/certbot/.nginx-reload
echo "[certbot-hook] Done — nginx reload signal sent."

