# READ

(https://www.thethingsindustries.com/docs/the-things-stack/host/docker/configuration/)[ThingStack LoRaWAN Instruction and Documentation for Docker]

Please ensure you look at localhost with self signed cert if doing on your personal machine, or if deploying to cloud virtual machine you undertand the process of using [https://certbot.eff.org/](LetsEncrypt) to secure your domain HTTPS endpoint.

## CHEAT SHEET

docker compose pull

chmod 644 ./config/stack

docker compose run --rm stack is-db migrate

docker compose run --rm stack is-db create-admin-user --id admin --email johndoe@gmail.com

docker compose run --rm stack is-db create-oauth-client \
  --id cli \
  --name "Command Line Interface" \
  --owner admin \
  --no-secret \
  --redirect-uri "local-callback" \
  --redirect-uri "code"

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

docker compose up
