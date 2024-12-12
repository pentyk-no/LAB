1.echo nikita
2.pwd > 2.txt
whoami >> 2.txt
3.ls -la > otchet/files/3.txt
4.touch 4.txt
code 4.txt
qwerty
touch 4.md
cat 4.txt >> 4.md
5.chmod o-r 4.txt
6.chmod 755 4.md
7.mv 4.txt ~/otchet/files 
mv 4.md ~/otchet/files 
8. sudo chown -c root ~/otchet/files/4.md
9. sudo useradd -m test_user
sudo groupadd wheel
sudo usermod -g wheel test_user
sudo chsh -s /bin/zsh test_user
10.sudo passwd test_user
11.sudo usermod -aG wheel test_user
12.cat /etc/passwd > ~/otchet/files/12.txt
13.chmod a+w ~/otchet/files/12.txt
14.su -P test_user
15.whoami >> /home/nikita_po/otchet/files/12.txt
pwd >> /home/nikita_po/otchet/files/12.txt
16.exit
17.whoami >> /home/nikita_po/otchet/files/12.txt
pwd >> /home/nikita_po/otchet/files/12.txt
18.exit
19.tail -n 2 ~/otchet/files/12.txt
20.sudo userdel -r test-user
21.find ~/ -maxdepth 2 -empty > ~/otchet/files/21.txt
22.sudo find / -maxdepth 3 -user root -name "dev*" > ~/otchet/files/22.txt
23.mkdir ~/test_find
mkdir ~/test_find/time
mkdir ~/test_find/permissions
24.touch ~/test_find/time/one.txt
touch ~/test_find/time/two.txt
touch -a -t 202401010000 ~/test_find/time/one.txt
touch -a -t 202410140000 ~/test_find/time/two.txt
25.touch ~/test_find/permissions/cant_write.txt
touch ~/test_find/permissions/can_execute.txt
chmod a+w ~/test_find/permissions/cant_write.txt
chmod a+w ~/test_find/permissions/can_execute.txt
26.find ~/test_find -atime +183 -delete
27.find ~/test_find -type f -perm 755 -exec chmod a-x {} +
28.man ls > man_ls.txt
29.grep -n '^$' man_ls.txt
30.grep '[0-9]' ~/man_ls.txt
31.grep "Richard M.Stallman" ~/man_ls.txt > ~/otchet/files/31.txt
32.wc -lc ~/man_ls.txt
33.ps -u $USER >~/otchet/files/33.txt
34.nano
35.pgrep nano
36.pkill nano
37.htop

 