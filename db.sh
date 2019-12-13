#!/bin/bash -x
docker rm -f skvn-db && \
docker run --name skvn-db -e POSTGRES_PASSWORD=sktl007001! -e POSTGRES_USER=seatuser -e POSTGRES_DB=sktl_inner_dev -p 5432:5432 -d postgres:9.6.15

