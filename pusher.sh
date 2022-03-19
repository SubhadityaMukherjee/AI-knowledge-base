#!/bin/bash
/home/erago/Documents/scripts/note-link-janitor/dist/index.js docs/
/home/erago/Documents/scripts/note-link-janitor/dist/index.js docs/Architectures/
/home/erago/Documents/scripts/note-link-janitor/dist/index.js docs/Applications/
/home/erago/Documents/scripts/note-link-janitor/dist/index.js docs/Federated/
git add . && git commit -m "update" && git push
