# miscellaneous.scripts
miscellaneous

# Use screen
```
type:
screen -S name 
for startinga new screen 
ctrl + a + d  for detaching the screen, ctrl + d for terminating
screen -ls 
screen -X -S SCREENID kill

for the list of screens 
screen -x {screen number} 
to re attach 
```


# Set up BOX 

- run on the hoffman2
```
rclone config
```

- on the MAC
```
1. install rclone. Instructions are here https://rclone.org/install/
2. run rclone authorize "box"
3. copy paster the token into terminal on hoffman2
4. finish the set up on hoffman2
```

# Run BOX

```
ssh dtn1
run screen
#check the directories
./rclone ls box:

~/code/miscellaneous.scripts/rclone copy -L -v --stats 30s raw.reads.batch3/ box:data/Kinisha.Gala2/raw.reads.batch3/

```

# Set up Gdrive
```
rclone config
select Gdrive and validate the link via browser
```

# run Google Drive
```
~/code/miscellaneous.scripts/rclone copy -L -v --stats 30s gdrive:/data/Kinisha.Gala/ ./
```

# Github
```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
cat ~/.ssh/id_rsa.pub
copy and paste in SSH keys at : https://github.com/settings/keys
```
- https://help.github.com/en/articles/adding-a-new-ssh-key-to-your-github-account
- https://help.github.com/en/articles/adding-a-new-ssh-key-to-your-github-account

