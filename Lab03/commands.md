#6. mkdir structure
#7. cd structure
mkdir 2023 2022 2021 2020 2019 2018
#(8,9,10).cd 2023
mkdir files
mkdir pictures
mkdir .passwords
cd
cd structure/2022/
mkdir files
mkdir pictures
mkdir .passwords
cd
cd structure/2021/
mkdir files
mkdir pictures
mkdir .passwords
cd
cd structure/2020/
mkdir files
mkdir pictures
mkdir .passwords
cd
cd structure/2019/
mkdir files
mkdir pictures
mkdir .passwords
cd
cd structure/2018/
mkdir files
mkdir pictures
mkdir .passwords
cd
cd structure/2023/files
touch data.md
cd
cd structure/2023/pictures
touch picture.png
cd
cd structure/2023/.passwords
touch .passwords.txt
cd
cd structure/2022/files
touch data.md
cd structure/2022/pictures
touch picture.png
cd
cd structure/2022/.passwords
touch .passwords.txt
cd
cd structure/2021/files
touch data.md
cd
cd structure/2021/pictures
touch picture.png
cd
cd structure/2021/.passwords
touch .passwords.txt
cd
cd structure/2020/files
touch data.md
cd
cd structure/2020/pictures
touch picture.png
cd
cd structure/2020/.passwords
touch .passwords.txt
cd
cd structure/2019/files
touch data.md
cd
cd structure/2019/pictures
touch picture.png
cd
cd structure/2019/.passwords
touch .passwords.txt
cd
cd structure/2018/files
touch data.md
cd
cd structure/2018/pictures
touch picture.png
cd
cd structure/2018/.passwords
touch .passwords.txt
cd
#(11).cd structure/2023/files
touch -a -t 202401010000.00 data.md
cd
cd structure/2022/files
touch -a -t 202401010000.00 data.md
cd
cd structure/2021/files
touch -a -t 202401010000.00 data.md
cd
cd structure/2020/files
touch -a -t 202401010000.00 data.md
cd
cd structure/2019/files
touch -a -t 202401010000.00 data.md
cd
cd structure/2018/files
touch -a -t 202401010000.00 data.md
cd
#12.cd structure/2023/.passwords
touch -m -t 202306100000.00 .passwords.txt
cd
cd structure/2022/.passwords
touch -m -t 202206100000.00 .passwords.txt
cd
cd structure/2021/.passwords
touch -m -t 202106100000.00 .passwords.txt
cd
cd structure/2020/.passwords
touch -m -t 202006100000.00 .passwords.txt
cd
cd structure/2019/.passwords
touch -m -t 201906100000.00 .passwords.txt
cd
cd structure/2018/.passwords
touch -m -t 201806100000.00 .passwords.txt
cd 
#13. cp -r ~/structure/2023 ~/Downloads/2025
#14. cd Downloads/2025/.passwords
touch -m -t 202506100000.00 .passwords.txt
#15. cp -r ~/Downloads/2025 ~/structure
#16. mv ~/structure/2025 ~/structure/2024
#17. mv 2024/pictures/picture.png 2024/pictures/image.png
mv 2023/pictures/picture.png 2023/pictures/image.png
mv 2022/pictures/picture.png 2022/pictures/image.png
mv 2021/pictures/picture.png 2021/pictures/image.png
mv 2020/pictures/picture.png 2020/pictures/image.png
mv 2019/pictures/picture.png 2019/pictures/image.png
mv 2018/pictures/picture.png 2018/pictures/image.png
#18. 2024 ~/Documents
2018 ~/Documents
#19. rmdir ~/Documents/2024
#20. rm -r  ~/Documents/2024
#21.cat > ~/structure/2019/files/data.md                                                                                       18:59:15
Hello.
#22. nano ~/structure/2020/files/data.md
Good luck
#23. code ~/structure/2021/files/data.md
WoW.
#24. cat ~/structure/2020/files/data.md >> ~/structure/2022/files/data.md
#25. cd structure
mkdir soft_links
mkdir hard_links
#26. ln -s {2018..2024} ~/structure/soft_links
#27.cd hard_links
ln ~/structure/2020/files/data.md
ln  ~/structure/2021/.passwords/.passwords.txt
#28.cd ~/structure/
mkdir archives
#30. mv ~/Downloads/image.jpg ~/structure/archives
#31. tar -c -v -f image.tar image.jpg                         17:00:08
tar -c -v -f image.tar.gz image.jpg
tar -c -v -f image.tar.bz2 image.jpg
#32. zip -e -r structure.zip ~/structure 