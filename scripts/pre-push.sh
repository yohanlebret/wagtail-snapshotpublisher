#!/usr/bin/env sh

echo "Running pre-push hook"
docker-compose run --rm web coverage run manage.py test

# $? stores exit value of the last command
if [ $? -ne 0 ]; then
    printf "\033[1;31mUnittest must pass before commit!\033[0m\n"
    exit 1
fi

printf "\033[1;32mUnitest - Passed\033[0m\n"

docker-compose run --rm web coverage report  --fail-under=85

if [ $? -ne 0 ]; then
    printf "\033[1;31mCoverage is under 90%%\033[0m\n"
    exit 1
fi

printf "\033[1;32mCoverage - Passed\033[0m\n"
