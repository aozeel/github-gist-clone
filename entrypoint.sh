if [ "$DATABASE" = "postgres"]
then
     echo "Waiting for postgres..."

     while ! nc -z $SQL_HOST $SQL