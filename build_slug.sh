mkdir slug
cp -R webapp/* slug
tar czfv slug.tgz ./slug
rm -rf slug/*