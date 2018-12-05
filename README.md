# miscellaneous.scripts
miscellaneous

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


