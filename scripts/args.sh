#!/bin/bash
echo "with \$@:"
for arg in "$@"; do
echo " [$arg]"
done

echo "with \$*:"
for arg in "$*"; do
echo " [$arg]"
done
