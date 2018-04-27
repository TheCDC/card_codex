mkdir app
cp -R webapp/dist/app/* app
rm slug.tgz
tar czfv slug.tgz ./app
# tar --strip-components 1 -xvf slug.tgz
# https://stackoverflow.com/questions/939982/how-do-i-tar-a-directory-of-files-and-folders-without-including-the-directory-it/39530409#39530409
# find webapp -printf "%P\n" -type f -o -type l -o -type d | tar -czf slug.tgz --no-recursion -C webapp -T -
rm -rf app
