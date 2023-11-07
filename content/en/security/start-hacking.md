---
title: Start hacking (Ethical hacking course)
lang: en
layout: post
date: 2023-11-07
---


### What I have learned

During the Ethical Hacking course, I learned that:

(1) Practice makes perfect.

(2) Knowing the right tools (and how to use them) is essential.

(3) Without knowing the command line (for both Linux and Windows) you are out of the loop. That's the place to start.



### Attack process

In the scope of course most of the attack were quite similar and consisted of the following stages:

(1) **Reconnaissance.**<br>
    Finding information about target using the any information source available. This phase has been omitted from the scope of the course.

(2) **Scanning/enumeration.**<br>
    Find computers on the network, the services they are running, software versions, operating systems, etc. It also includes determining whether the services found with specific versions on a given operating system are known to be vulnerable. For scanning, my friend during the course was the program [nmap](https://nmap.org/book/man.html). When searching for vulnerabilities, firstly databases are checked, and if unsuccessful, then the internet is searched.

(3) **Exploitation.**<br>
    Use the identified weakness to your advantage. This may be downloading a file or getting a shell on a machine. I have used the [Metasploit Framework](https://www.metasploit.com/) many times and especially [msfvenom](https://docs.metasploit.com/docs/using-metasploit/basics/how-to-use-msfvenom.html) for getting the shell on machines.

(4) **Post-exploitation.**<br>
    You are now in the system. You can start again from the survey and discover machines that were not visible from the previous position in the network. You can also create additional backdoors and shortcuts into the system and also elevate your privileges.

### My motto that I take away from the course is:

- Scan, scan, scan
- Enumerate, Enumerate, Enumerate

### Best sources on information

Most of the time during the course I was looking for information about certain services, how they work and what their possible vulnerabilities are. I consulted a lot of resources, but I'll mention one that I find the most influential, namely [HackTricks](https://book.hacktricks.xyz/), which seems very comprehensive (at least from a course perspective) and also provides a pentesting methodology. 

### Platforms to learn

After completing the course, I looked into where I could further my learning and found three platforms [pwn.college](https://pwn.college/), [HackTheBox](https://www.hackthebox.com/) and [TryHackMe](https://tryhackme.com/). To date, I only have enough experience with pwn.college. This platform is very beginner friendly. It starts from basic interaction with programs and builds up to reverse engineering. I haven't finished it yet because there is a ton of content, but so far it looks promising.