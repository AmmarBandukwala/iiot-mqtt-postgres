
# LoRaWAN Network Server Deployment Notes

## Reference

[ThingStack LoRaWAN Instruction and Documentation for Docker](https://www.thethingsindustries.com/docs/the-things-stack/host/docker/configuration/)

If running locally, use a self-signed certificate. For cloud deployments, secure your domain's HTTPS endpoint using [LetsEncrypt](https://certbot.eff.org/).

---

## Cheat Sheet

### Pull Docker Images

```sh
docker compose pull
```

### Set Permissions

```sh
chmod 644 ./config/stack
```

### Database Migration

```sh
docker compose run --rm stack is-db migrate
```

### Create Admin User

```sh
docker compose run --rm stack is-db create-admin-user --id admin --email johndoe@gmail.com
```

### Create OAuth Client (CLI)

```sh
docker compose run --rm stack is-db create-oauth-client \
  --id cli \
  --name "Command Line Interface" \
  --owner admin \
  --no-secret \
  --redirect-uri "local-callback" \
  --redirect-uri "code"
```

### Create OAuth Client (Console)

```sh
SERVER_ADDRESS=https://CHANGEME.com
ID=console
NAME=Console
CLIENT_SECRET=console
REDIRECT_URI=${SERVER_ADDRESS}/console/oauth/callback
REDIRECT_PATH=/console/oauth/callback
LOGOUT_REDIRECT_URI=${SERVER_ADDRESS}/console
LOGOUT_REDIRECT_PATH=/console

docker compose run --rm stack is-db create-oauth-client \
  --id ${ID} \
  --name "${NAME}" \
  --owner admin \
  --secret "${CLIENT_SECRET}" \
  --redirect-uri "${REDIRECT_URI}" \
  --redirect-uri "${REDIRECT_PATH}" \
  --logout-redirect-uri "${LOGOUT_REDIRECT_URI}" \
  --logout-redirect-uri "${LOGOUT_REDIRECT_PATH}"
```

### Start the Stack

```sh
docker compose up
```
