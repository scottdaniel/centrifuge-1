#!/bin/bash

echo "QUERY \"${QUERY}\""
echo "INDEX  \"${INDEX}\""
echo "EXCLUDE_TAXIDS \"${EXCLUDE_TAXIDS}\""
echo "MIN_ABUNDANCE \"${MIN_ABUNDANCE}\""

sh run.sh ${QUERY} ${INDEX} ${EXCLUDE_TAXIDS} ${MIN_ABUNDANCE}
