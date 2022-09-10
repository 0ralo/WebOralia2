#!/bin/bash
exec celery -A WebOralia2.celery worker -n worker1@%n