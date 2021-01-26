# Start Mincraft server AWS   

Start Minecraft locally on your computer using docker   
```docker run -d -p 25565:25565 --name mc -e EULA=TRUE itzg/minecraft-server```   

## AWS   
1. you'll need to start an instance and install docker   
2. then create AMI from that instance   
3. update the AMI in the instance ID in the script   
4. change the instance type per your load / number of players   
5. create a security group with the IP's of the players
6. create pem file
7. add the security group and key file to the ```create_instance_minecraft``` function   

Start the Minecraft instance script (choose the function you need)   
```launch_minecraft_instance.py```   

## Persistent data (not included)   
You'll need to add persistent data to save your game