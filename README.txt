commands to run the docker container

docker build -t prototype .
docker run --rm -p 85:5000 prototype

Then I use postman to run commands as of right now I just have a mine command.
Since it is running on the localhost I just use http://localhost:85//mine to mine
new blocks.  If you want to change the amount mined you can change the range on the 
for loop in the mine() function.


