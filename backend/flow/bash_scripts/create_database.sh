# File to create a Database and User in psql


# Check whether the system has psql
if ! command -v psql &> /dev/null
then 
  echo "psql is not installed, installing..."
  sudo apt-get install postgresql -y
fi

read -p "Enter database name: " database
read -p "Enter username: " user
read -p "Enter password for user: " password

# Create the database with the arguments provided
su - postgres <<EOF
psql

-- Executing psql commands

CREATE DATABASE $database;
CREATE USER $user WITH PASSWORD'$password';
GRANT ALL PRIVILEGES ON DATABASE $database TO $user;

-- Check that the database and user were created
\l
SELECT pg_sleep(5);
\q
EOF
