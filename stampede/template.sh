#!/bin/bash

echo "QUERY \"${QUERY}\""
echo "INDEX  \"${INDEX}\""
echo "EXCLUDE_TAXIDS \"${EXCLUDE_TAXIDS}\""
echo "MIN_ABUNDANCE \"${MIN_ABUNDANCE}\""
echo "FORMAT \"${FORMAT}\""

sh run.sh ${QUERY} ${INDEX} ${EXCLUDE_TAXIDS} ${MIN_ABUNDANCE} ${FORMAT}
