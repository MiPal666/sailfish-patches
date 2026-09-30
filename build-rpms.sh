#!/bin/bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
VERSION="1.0.0"
OUT="$ROOT/_rpm-build"

rm -rf "$OUT"
mkdir -p "$OUT"/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS,stage}

make_source()
{
    NAME="$1"
    shift

    STAGE="$OUT/stage/${NAME}-${VERSION}"
    mkdir -p "$STAGE"

    for FILE in "$@"; do
        cp "$ROOT/$NAME/$FILE" "$STAGE/"
    done

    tar -C "$OUT/stage" -czf "$OUT/SOURCES/${NAME}-${VERSION}.tar.gz" "${NAME}-${VERSION}"
    cp "$ROOT/$NAME/rpm/${NAME}.spec" "$OUT/SPECS/"
}

make_source felis-sharp-caller-photo unified_diff.patch patch.json
make_source felis-phone-start-page unified_diff.patch patch.json main.qml

cd "$ROOT"
sfdk build-init

sfdk build-shell rpmbuild --define "_topdir $OUT" -bb "$OUT/SPECS/felis-sharp-caller-photo.spec"
sfdk build-shell rpmbuild --define "_topdir $OUT" -bb "$OUT/SPECS/felis-phone-start-page.spec"

echo
echo "Built RPMs:"
find "$OUT/RPMS" -type f -name '*.rpm' -print
