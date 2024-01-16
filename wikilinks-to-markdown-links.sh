#!/bin/bash

:'
Matching:

\[\[            inside of double bracket literals
  (             capture...
    [^          all characters that are not..
      \[\|      left bracket or pipe literal
    ]
    +           one or more times
  )
\|              followed by a pipe literal
  (             capture...
    [^          all characters that are not...
      \[        left bracket literal
    ]
    +           one or more times
  )
\]\]

Second one is the same but without the description
'

sed -r -i 's,\[\[([^\[\|]+)\|([^\[]+)\]\],[\2](\1),g' $@
sed -r -i 's,\[\[([^\[\|]+)\]\],[\1](\1),g' $@