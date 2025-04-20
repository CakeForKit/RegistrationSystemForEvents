#!/bin/bash

pytest --asyncio-mode=auto \
       --cov=/app/src \
       --cov-report=term-missing \
       --cov-report=html \
       /app/src/tests