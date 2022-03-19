#!/bin/bash
/home/erago/Documents/scripts/note-link-janitor/dist/index.js docs/
/home/erago/Documents/scripts/note-link-janitor/dist/index.js docs/architectures/
/home/erago/Documents/scripts/note-link-janitor/dist/index.js docs/applications/
/home/erago/Documents/scripts/note-link-janitor/dist/index.js docs/federated/
git add . && git commit -m "update" && git push
