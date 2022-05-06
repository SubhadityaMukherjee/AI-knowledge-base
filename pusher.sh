#!/bin/bash
python3 backlink_reset.py
/home/erago/.yarn/bin/note-link-janitor docs/
#/home/erago/.yarn/bin/note-link-janitor docs/architectures/
#/home/erago/.yarn/bin/note-link-janitor docs/applications/
#/home/erago/.yarn/bin/note-link-janitor docs/federated/
git add . && git commit -m "update" && git push
