kill_process=`sudo lsof -i:80 | awk 'NR == 2 {print $2}'`
kill -9 $kill_process

export FLASK_APP="/home/ec2-user/api/app.py"
flask run --host=0.0.0.0 --port 80
