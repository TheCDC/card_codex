#
# https://devcenter.heroku.com/articles/platform-api-deploying-slugs#create-the-slug
CHECKSUM=`shasum --algorithm 256 slug.tgz | python3 -c "import sys;[print(i.split(' ')[0]) for i in sys.stdin]"`
echo "Publish to platform"
RESPONSE=`curl -X POST \
-H 'Content-Type: application/json' \
-H 'Accept: application/vnd.heroku+json; version=3' \
-d "{\"checksum\":\"$CHECKSUM\", \"process_types\":{\"web\":\"./app\"}}" \
-n https://api.heroku.com/apps/card-codex-dev/slugs`
echo $RESPONSE
URL=`echo $RESPONSE | python -c "import json;import sys;print(json.load(sys.stdin)['blob']['url'])"`
ID=`echo $RESPONSE | python -c "import json;import sys;print(json.load(sys.stdin)['id'])"`
echo "URL=$URL"
echo "ID=$ID"


echo "Upload slug"
UPLOADRESPONSE=`curl -X PUT \
-H "Content-Type:" \
--data-binary @slug.tgz \
$URL`


echo "Release slug"
SLUGJSON="{\"slug\":\"$ID\"}"
echo "SLUGJSON=$SLUGJSON"
curl -X POST \
-H "Accept: application/vnd.heroku+json; version=3" \
-H "Content-Type: application/json" \
-d $SLUGJSON \
-n https://api.heroku.com/apps/card-codex-dev/releases
echo "========== Done =========="