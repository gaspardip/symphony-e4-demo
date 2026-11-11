#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
printf '{"project":"symphony-e4-demo","tests":%s,"head":"%s"}\n' \
  "$(find tests -name 'test_*.py' | wc -l | tr -d ' ')" "$(git rev-parse HEAD)"
