#!/bin/bash
/home/erago/.yarn/bin/note-link-janitor/dist/index.js docs/
/home/erago/.yarn/bin/note-link-janitor/dist/index.js docs/architectures/
/home/erago/.yarn/bin/note-link-janitor/dist/index.js docs/applications/
/home/erago/.yarn/bin/note-link-janitor/dist/index.js docs/federated/
git add . && git commit -m "update" && git push
